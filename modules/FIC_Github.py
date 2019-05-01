# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import github3
from modules.FIC_Logger import FICLogger
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_DataVault import FICDataVault
from modules.config import GIT_TOKEN
from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
from git import Repo
import os
import json
from modules.FIC_DataVault import FICDataVault


class FICGithub(FICFileHandler, FICLogger, FICDataVault):

    def __init__(self, team_name, repo_name):
        FICLogger.__init__(self)
        FICFileHandler.__init__(self)
        FICDataVault.__init__(self)
        self.team_name = team_name
        self.repo_name = repo_name
        self.token_counter = 0
        self._get_os_var()
        self._token = os.environ.get(GIT_TOKEN[self.token_counter])
        self._gh = self._auth()
        self.repo_data = self.read_repo()
        self.repo = Repo("..")

    def _auth(self):
        return github3.login(token=self._token)

    def read_repo(self):
        return self._init_github(self._gh, self.team_name, self.repo_name)

    def _init_github(self, *args):
        self.repo_data = github3.GitHub.repository(args[0], args[1], args[2])
        return self.repo_data

    def _get_os_var(self):
        for var in os.environ:
            # append the OS.VAR to the list in case of no duplicate
            if "GIT_TOKEN" in var and var not in GIT_TOKEN:
                GIT_TOKEN.append(var)
        self.LOGGER.info("The list of available tokens: %s", GIT_TOKEN)

    def _get_reset_time(self):
        from datetime import datetime
        reset_time = datetime.fromtimestamp(self._gh.rate_limit()['rate']['reset'])
        self.LOGGER.info("Rate limit reset in: %s", reset_time - datetime.now())
        return reset_time

    def limit_checker(self):
        limit_requests = self._gh.ratelimit_remaining

        if limit_requests < 5 and len(GIT_TOKEN) > 1:
            # switch token
            if self._switch_token():
                return True
            else:
                # check if the rate limit was reset for the second use of a token
                if limit_requests < 5:
                    print(self._get_reset_time())
                    return False
                else:
                    return True
        # check the reset time in case of a single token
        elif limit_requests < 5:
            print(self._get_reset_time())
            return False
        # return True in case of limit request not reached
        else:
            return True

    def _switch_token(self):
        # get next token
        switch = self._get_token()
        # re-logging with the new token
        self._token = os.environ.get(GIT_TOKEN[self.token_counter])
        self._gh = self._auth()
        self.LOGGER.info("The token was changed.")
        return switch

    def _get_token(self):
        # in case of the next token but not the last
        if self.token_counter < len(GIT_TOKEN) - 1:
            self.token_counter += 1
            self.LOGGER.info("Changing token with: %s", GIT_TOKEN[self.token_counter])
            return True
        # in case of the last token
        elif self.token_counter == len(GIT_TOKEN) - 1:
            self.token_counter = 0
            self.LOGGER.info("Changing token with: %s", GIT_TOKEN[self.token_counter])
            return False

    def pull(self):
        self.LOGGER.info("pulling changes from {} -> Branch {}".format(self.repo.remotes.origin.url, self.repo.active_branch))
        return self.repo.remotes.origin.pull(refspec=self.repo.active_branch)

    def add(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
        self.repo.git.add([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH], update=True)
        return self.check_for_changes()

    def check_for_changes(self):
        if not self.repo.index.diff("HEAD"):
            self.LOGGER.info("Nothing staged for commit. has the data or files changed?")
            return False
        return True

    def commit(self):
        from datetime import datetime
        self.LOGGER.info("Committing changes with message: Changelog: %s", str(datetime.utcnow()))
        return self.repo.index.commit("Changelog: " + str(datetime.utcnow()))

    def push(self):
        self.LOGGER.info("Summary of pull: {}".format(FICGithub.pull(self)[0]))
        if FICGithub.add(self):
            self.LOGGER.info("Summary of commit {}".format(FICGithub.commit(self)))
            self.LOGGER.info("pushing changes to {}  on branch  {}".format(self.repo.remotes.origin.url, self.repo.active_branch))
            self.LOGGER.info("Summary of push: {}".format(self.repo.remotes.origin.push(refspec=self.repo.active_branch)[0].summary))

    def revert_modified_files(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
        return self.repo.git.checkout([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH])

    def get_repo_url(self):
        return self.repo_data.svn_url

    def repo_type(self):
        return json.load(self.load(None, "repositories.json")).get("Github").get(self.repo_name).get("configuration").get("type")


    def repo_team(self):
        self.team_name = json.load(self.load(None, "repositories.json")).get("Github").get(self.repo_name).get("team")

    def repo_files(self):
        return json.load(self.load(None, "repositories.json")).get("Github").get(self.repo_name).get("configuration").get("folders-to-check")

    def get_sha(self, commit):
        self.commit_sha = commit.sha

    def get_message(self, commit):
        self.commit_message = commit.message

    def get_date(self, commit):
        self.commit_date = commit.commit.author.get("date")

    def get_author(self, commit):
        self.commit_author = commit.commit.author.get("name")

    def get_author_email(self, commit):
        self.commit_author_email = commit.commit.author.get("email")

    def get_url(self, commit):
        self.commit_url = commit.url

    def get_files(self):
        self.commit_files_changed = []
        for item in (range(len(self.repo_data.commit(sha=self.commit_sha).files))):
            self.commit_files_changed.append(self.repo_data.commit(sha=self.commit_sha).files[item].get('filename'))

    def store_data(self, current_commit):
        self.get_sha(current_commit)
        self.get_message(current_commit)
        self.get_date(current_commit)
        self.get_author(current_commit)
        self.get_author_email(current_commit)
        self.get_url(current_commit)
        self.get_files()

    def construct_commit(self):
        self.list_of_commits.update({self.commit_number: {'sha': self.commit_sha,
                                                          'url': self.commit_url,
                                                          'author': self.commit_author,
                                                          'author_email': self.commit_author_email,
                                                          'message': self.commit_message,
                                                          'date': self.commit_date,
                                                          'files': self.commit_files_changed}})

    def last_checked(self):
        self.last_check = json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json")).get("0").get("last_checked")

    def local_version(self):
        self.release_date = json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json")).get("0").get("last_release").get("version")

    def not_tag(self):
        pass

    def build_puppet(self):
        pass

    def tag(self):
        pass

    def commit_keyword(self):
        pass

    def repo_selector(self):
        if self.repo_type() == "no-tag":
            self.not_tag()

        elif self.repo_type() == "tag":

            if self.repo_name == "build-puppet":
                self.build_puppet()
            else:
                self.tag()

        elif self.repo_type() == "commit-keyword":
            self.commit_keyword()
        else:
            print("Repo type not defined for %s", self.repo_name)

    # the main method to iterate through the commits
    def commit_iterator(self):
        for current_commit in self.repo_data.commits(since=self.last_check, until=self.release_date):
            self.store_data(current_commit)
            self.construct_commit()
            self.commit_number += 1

    # the main method to iterate through the Git repository
    def repo_iterator(self):
        for repo in json.load(self.load(None, "repositories.json")).get("Github"):
            self.repo_name = repo


# for testing
a = FICGithub('mozilla-releng', 'OpenCloudConfig')
print(a.get_repo_url())
print(a.repo_type())
a.commit_date = '2019-04-13'
a.release_date = None
a.commit_number = 0
a.repo_iterator()
print(a.commit_iterator())
print(a.list_of_commits)
