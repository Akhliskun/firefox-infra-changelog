import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta
import requests
import json
import re

# Create a Github instance:
TOKEN = os.environ.get("GIT_TOKEN")
git = Github(TOKEN)

def filter_commit_data(repository_name, repository_team):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function from 're' library
    :param commit: json style content required to be filtered
    :return: filtered json data
    TODO: please add the exception blocks since the script fails when it can't pull a data:
    (e.g raise self.__createException(status, responseHeaders, output)
            github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """
    repo_dict = {}
    number = 1
    repository_path = repository_team + repository_name
    for commit in git.get_repo(repository_path).get_commits():    # here we should add ".get.commits(since=last_run)"
        each_commit = {}
        author_info = {}
        commit_sha = commit.sha
        commiter_name = commit.author.login
        commit_url = commit.url
        commiter_email = commit.committer.email
        commit_message = commit.commit.message
        commit_date = str(commit.commit.author.date)
        message = re.sub('[*\n\r]', ' ', commit_message)
        author_info.update({'sha': commit_sha,
                            'url': commit_url,
                            'commiter_name': commiter_name,
                            'commiter_email': commiter_email,
                            'commit_message': message,
                            'commit_date': commit_date
                            })
        each_commit.update({number: author_info})
        git_json_filename = "{}.json".format(repository_name)

        try:               # it will append the new commit to the .json file
            with open(git_json_filename) as f:
                repo_dict = json.load(f)

            repo_dict.update(each_commit)

            with open(git_json_filename, "w") as json_file:
                json.dump(repo_dict, json_file, indent=2)
            json_file.close()
        except:            # it will create a new .json file since it is not exist already
            with open(git_json_filename, "w") as json_file:
                json.dump(repo_dict, json_file, indent=2)
            json_file.close()

        number += 1

def create_files_for_git():
    """
    Main GIT function. Takes every Git repo from repositories.json and writes all the commit data of each repo in a
    separate json file and generates a MD file for each repo as well.
    :return: the end result is a .json and a .md file for every git repository. can be found inside git_files/
    """
    for repo in repositories["Github"]:
        repository_name = repo
        repository_team = repositories["Github"][repo]["team"]
        filter_commit_data(repository_name, repository_team)


if __name__ == "__main__":
    TOKEN = os.environ.get("GIT_TOKEN")
    git = Github(TOKEN)
    repositories_data = open('./repositories-test.json').read()
    repositories = json.loads(repositories_data)
    create_files_for_git()