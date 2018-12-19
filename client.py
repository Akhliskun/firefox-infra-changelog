import os
import re
import json
import requests
from os import listdir
from github import Github
from os.path import isfile, join
from datetime import datetime, timedelta
import sys

lastWeek = datetime.now() - timedelta(days=14)
current_dir = os.path.dirname(os.path.realpath(__file__))


def limit_checker():
    """
    This function checks if your limit requests is not exceeded.
    Every time when this function is called, it returns 1 in case of your requests limit is not exceeded,
    otherwise it wait for the reset time to pass.
    :return: it returns 1 if your limit requests is not exceeded
    """
    rate_limit = git.rate_limiting[0]
    unix_reset_time = git.rate_limiting_resettime
    reset_time = datetime.fromtimestamp(unix_reset_time)
    if rate_limit >= 5:
        sys.stdout.write("\rRate limit is: " + str(rate_limit))
        sys.stdout.flush()
        return 1
    else:
        try:
            print("\nYou have reached the requests limit!")
            print("\nThe requests limit is reset to: " + str(reset_time))
            while rate_limit < 5000 and reset_time >= datetime.now():
                unix_reset_time = git.rate_limiting_resettime
                reset_time = datetime.fromtimestamp(unix_reset_time)
            print("\nThe requests limit has been reset! ")
            return 1
        except:
            print("\nThe requests limit is reset to: " + str(reset_time))


def create_files_for_git(repositories_holder):
    """
    Main GIT function. Takes every Git repo from a .json file which is populated with repositories and writes all
    the commit data of each repo in a.
    creates a json and MD file for each repo as well.
    :param: repositories_holder: Expects a .json file that contains a list of repositories
    :return: The end result is a .json and a .md file for every git repository. can be found inside git_files/
    """
    for repo in repositories_holder["Github"]:
        repository_name = repo
        repository_team = repositories_holder["Github"][repo]["team"]
        repository_version = get_version(repository_name, repository_team)
        version_in_puppet = 0
        folders_to_ignore = repositories_holder["Github"][repo]["configuration"]["folders-to-ignore"]
        files_to_ignore = repositories_holder["Github"][repo]["configuration"]["files-to-ignore"]
        repository_type = repositories_holder["Github"][repo]["configuration"]["type"]
        print("\nWorking on repo: {}".format(repository_name))
        try:
            repository_version_path = repositories["Github"][repo]["configuration"]["version-path"]
            version_in_puppet = get_version_from_build_puppet(repository_version_path, repository_name)
            files_to_care_for = repositories_holder["Github"][repo]["configuration"]["files-we-care-about"]
        except KeyError:
            pass
        if repository_version is not None:
            try:
                if repository_version["LatestRelease"]["version"] == version_in_puppet:
                    print("\nNo new changes came into production!")
                else:
                    filter_git_commit_data(
                        repository_name,
                        repository_team,
                        repository_version,
                        folders_to_ignore,
                        files_to_ignore,
                        files_to_care_for
                    )
            except TypeError:
                pass
        else:
            filter_git_commit_data(
                repository_name,
                repository_team,
                repository_version,
                folders_to_ignore,
                files_to_ignore,
                files_to_care_for
            )
        try:
            create_md_table(repository_name, "git_files")
        except:
            print("\nFailed to create markdown table!")
            pass


def get_version(repo_name, repo_team):
    """
    :param repo_name: repository name
    :param repo_team: repository team
    :return: a dictionary with information from the last two release version: latestRelease and previousRelease
    """
    repo_path = repo_team + repo_name
    iteration = 0
    if limit_checker() == 1:        # check if the requests limit is not exceeded
        for tags in git.get_repo(repo_path).get_tags():
            version = tags.name
            sha = tags.commit.sha
            date = tags.commit.commit.last_modified
            author = tags.commit.author.login
            if iteration == 0:
                latestrelease = {"version": version,
                                 "sha": sha,
                                 "date": date,
                                 "author": author
                                 }
                iteration = 1
            elif iteration == 1:
                previousrelease = {"version": version,
                                   "sha": sha,
                                   "date": date,
                                   "author": author
                                   }
                return {"LatestRelease": latestrelease, "PreviousRelease": previousrelease}


def get_version_from_build_puppet(version_path, repo_name):
    """
    :param: version_path: Path to the requierments.txt where the version number is stored
    :param: repo_name: The repo for which we are checking the version.
    :return: Returns the version number that is stored in build-puppet for each *scriptworker
    """
    if limit_checker() == 1:        # check if the requests limit is not exceeded
        file_to_string = requests.get(version_path).text.split()
        for word in file_to_string:
            if repo_name in word:
                version_in_puppet = re.split("\\b==\\b", word)[-1]
                # the next check makes sure to only return the version in case the repo name appears multiple times
                if version_in_puppet != repo_name:
                    return version_in_puppet


def extract_files_from_commit(commit):
    """
    Helper Function!
    This creates a list with all the files that were modified in a commit.
    :param commit: Takes as a parameter a commit
    :return: returns a list  with the commit files modified in the commit.
    """
    return [commit.files[i].filename for i in range(0, len(commit.files))]


def compare_files(first_list, second_list):
    """
    Helper Function!
    Compares two lists that should contain the path + filename of the modified files. The two lists are mutable.
    :param first_list: First lists.
    :param second_list:  Second list
    :return: returns boolean value in case a match is found.
    """
    if set(first_list).intersection(second_list):
        return True
    else:
        return False


def extract_common_files(first_list, second_list):
    """
    Helper Function!
    Compares two lists that should contain the path + filename of the modified files. The two lists are mutable.
    :param first_list: First lists.
    :param second_list:  Second list
    :return: a list of mutuale files in the input lists.
    """
    return set(first_list).intersection(second_list)


def compare_folders(first_list, second_list):
    """
    Helper Function!
    Compares two lists that should contain the path of the files.
    The second_list can accept "path + filename" but the first_list cannot.
    The two lists are NOT mutable.
    :param first_list: First lists that should contains paths
    :param second_list:  Second list that should contain paths + filename.
    :return: returns boolean value in case a match is found.
    """
    for ii in range(0, len(first_list)):
        for jj in range(0, len(second_list)):
            if first_list[ii] in second_list[jj]:
                return True
            else:
                return False


def extract_common_folders(first_list, second_list):
    """
    Helper Function!
    Compares two lists that should contain the path of the files.
    The second_list can accept "path + filename" but the first_list cannot.
    The two lists are NOT mutable.
    :param first_list: First lists that should contains paths
    :param second_list:  Second list that should contain paths + filename.
    :return: returns a list that should contain the common_folders.
    """
    common_folders = []
    for ii in range(0, len(first_list)):
        for jj in range(0, len(second_list)):
            if first_list[ii] in second_list[jj]:
                common_folders = first_list[ii]
            else:
                pass

    return common_folders


def filter_git_commit_data(repository_name,
                           repository_team,
                           repository_version,
                           repository_type,
                           folders_to_ignore,
                           files_to_ignore,
                           files_to_care_for
                           ):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function from 're' library
    :param repository_team:
    :param repository_name:
    :param repository_version: dictionary that contains data from the last 2 releases
    :return: Filtered json data
    TODO: please add the exception blocks since the script fails when it can't pull a data:
    (e.g raise self.__createException(status, responseHeaders, output)
            github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """

    git_json_filename = "{}.json".format(repository_name)
    repository_path = repository_team + repository_name
    try:
        with open(current_dir + "/git_files/" + git_json_filename, "r") as commit_json:
            repo_dict = json.load(commit_json)
            number = len(repo_dict)
            last_checked = repo_dict["0"]["lastChecked"]
            repo_dict.update({"0": {"lastChecked": str(datetime.utcnow()),
                                    "last_two_releases": repository_version}})
    except FileNotFoundError:
        repo_dict = {}
        last_checked = str(git.get_repo(repository_path).created_at)
        repo_dict.update({"0": {"lastChecked": str(datetime.utcnow()),
                                "last_two_releases": repository_version}})
        number = 1

    try:
        latest_release = datetime.strptime(repository_version["LatestRelease"]["date"], "%a, %d %b %Y %H:%M:%S GMT")
        previous_release = datetime.strptime(repository_version["PreviousRelease"]["date"], "%a, %d %b %Y %H:%M:%S GMT")
    except TypeError:
        previous_release = lastWeek
        pass

    ignore_list2 = []  # initialise a new list. Everything that did not pass the check will be appended here
    our_ignore_list = folders_to_ignore + files_to_ignore  # all files and folder we want to ignore
    our_care_list = files_to_care_for  # list of paths that we care about

    if repository_type == "tag" and limit_checker() == 1:
        for commit in git.get_repo(repository_path).get_commits(since=previous_release, until=latest_release):
            if limit_checker() == 1:
                each_commit = {}
                author_info = {}
                files_changed = []
                try:
                    commit_sha = commit.sha
                except ValueError:
                    commit_sha = "null"
                try:
                    commiter_name = commit.author.login
                except ValueError:
                    commiter_name = "null"
                try:
                    commiter_email = commit.committer.email
                except ValueError:
                    commiter_email = "null"
                try:
                    commit_message = commit.commit.message
                    commit_message = re.sub("[*\n\r]", " ", commit_message)
                except ValueError:
                    commit_message = "null"
                try:
                    commit_html_url = commit.html_url
                except ValueError:
                    commit_html_url = "null"
                try:
                    for entry in commit.files:
                        files_changed.append(entry.filename)
                except ValueError:
                    pass
                try:
                    commit_date = commit.commit.author.date
                except ValueError:
                    commit_date = "null"

                author_info.update({"sha": commit_sha,
                                    "url": commit_html_url,
                                    "commiter_name": commiter_name,
                                    "commiter_email": commiter_email,
                                    "commit_message": commit_message,
                                    "commit_date": str(commit_date),
                                    "files_changed": files_changed
                                    })
                each_commit.update({int(number): author_info})
                number += 1
                repo_dict.update(each_commit)
    elif repository_type == "no tag" and limit_checker() == 1:
        try:
            oldest_commit = datetime.strptime(last_checked, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            oldest_commit = datetime.strptime(last_checked, "%Y-%m-%d %H:%M:%S")

        newest_commit = datetime.utcnow()
        for commit in git.get_repo(repository_path).get_commits(since=oldest_commit, until=newest_commit):
            if limit_checker() == 1:
                each_commit = {}
                author_info = {}
                files_changed = []
                try:
                    commit_sha = commit.sha
                except:
                    commit_sha = "null"
                try:
                    committer_name = commit.author.login
                except:
                    committer_name = "null"
                try:
                    committer_email = commit.committer.email
                except:
                    committer_email = "null"
                try:
                    commit_message = commit.commit.message
                    commit_message = re.sub("[*\n\r]", " ", commit_message)
                except:
                    commit_message = "null"
                try:
                    commit_html_url = commit.html_url
                except:
                    commit_html_url = "null"
                try:
                    for entry in commit.files:
                        files_changed.append(entry.filename)
                except:
                    pass
                try:
                    commit_date = commit.commit.author.date
                except:
                    commit_date = "null"

                author_info.update({"sha": commit_sha,
                                    "url": commit_html_url,
                                    "commiter_name": committer_name,
                                    "commiter_email": committer_email,
                                    "commit_message": commit_message,
                                    "commit_date": str(commit_date),
                                    "files_changed": files_changed
                                    })
                each_commit.update({int(number): author_info})
                number += 1
                repo_dict.update(each_commit)
                repo_dict.update({"0": {"lastChecked": str(commit_date)}})

    git_json_filename = "{}.json".format(repository_name)
    json_file = open(current_dir + "/git_files/" + git_json_filename, "w")
    json.dump(repo_dict, json_file, indent=2)
    json_file.close()


def create_files_for_hg(repositories_holder):
    """
    Main HG function. Takes every Mercurial repo from a .json file which is populated with repositories and writes all
     the commit data of each repo in a.
    creates a json and MD file for each repo as well.
    :param: repositories_holder: Expects a .json file that contains a list of repositories
    :return: The end result is a .json and a .md file for every git repository. can be found inside hg_files/
    """
    for repo in repositories_holder["Mercurial"]:
        repository_name = repo
        repository_url = repositories_holder["Mercurial"][repo]["url"]
        filter_hg_commit_data(repository_name, repository_url)
        create_md_table(repository_name, "hg_files")


def filter_hg_commit_data(repository_name, repository_url):
    """
    This function takes a repository url and push type and returns a dictionary that contains changes in that specific
    repository.
    The HG API also supports xml and rss.
    Example:
    example = get_push("https://hg.mozilla.org/build/nagios-tools/", "json-log")
    This will be later used to get the commits from https://hg.mozilla.org/
    :param repository_name: name of the repository
    :param repository_url: Link of the repository, eg: https://hg.mozilla.org/build/nagios-tools/
    :return: Returns a dictionary that contains the commits in the provided hg_repository_name
    """
    request_url = repository_url + "json-log"
    hg_repo_data = {}
    commit_number = 0
    print("\nWorking on repo:", repository_name)
    hg_repo_data.update({commit_number: {"lastChecked": str(datetime.utcnow())}})
    data = json.loads(requests.get(request_url).text)
    commit_number += 1

    for entry in data["changesets"]:
        node = entry["node"]
        url = repository_url + "pushloghtml?changeset=" + node[:12]
        commiter = entry["user"]
        commiter_name = commiter.split('<')[0]
        commiter_email = extract_email(commiter)
        commit_message = entry["desc"]
        message = re.sub("[*\n\r]", " ", commit_message)
        date = entry["date"]
        hg_repo_data.update({commit_number: {
            "sha": node,
            "url": url,
            "commiter_name": commiter_name,
            "commit_email": commiter_email,
            "commit_message": message,
            "commit_date": datetime.utcfromtimestamp(date[0]).strftime('%Y-%m-%d %H:%M:%S')
        }})
        commit_number += 1
    hg_json_filename = "{}.json".format(repository_name)
    json_file = open(current_dir + "/hg_files/" + hg_json_filename, "w")
    json.dump(hg_repo_data, json_file, indent=2)
    json_file.close()


def extract_email(commit_email):
    """
    Helper function!
    Takes as parameter a string that contains between "<" and ">" an email that needs to be extracted.
    The function uses find to search for the beginning of the email (that starts with "<") and adds the lengths of the
    "<" so that returned email doesn't contain the "<" symbol and rfind to find the ending character ">". Both find and
    rfind return the index where the carachters "<" and ">" are placed so when you do return commit_email with
    [start_char_index:ending_char_index] the string shrinks to what's between the characters.
    :param commit_email: String that contains an email
    :return: String that contains only the email
    """
    return commit_email[commit_email.find("<") + len("<"):commit_email.rfind(">")]


def create_md_table(repository_name, path_to_files):
    """
    Uses 'repository_name' parameter to generate markdown tables for every json file inside path_to_files parameter.
    :param repository_name: Used to display the repo name in the title row of the MD table
    :param path_to_files: Used to store path to json files (git_files, hg_files)
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open(current_dir + "/{}/".format(path_to_files) + "{}.json".format(repository_name)).read()
        data = json.loads(json_data)
        base_table = "| Commit Number | Commiter | Commit Message | Commit Url | Date | \n" + \
                     "|:---:|:----:|:----------------------------------:|:------:|:----:| \n"
        tables = {}
        try:
            version = data['0']["last_two_releases"]["LatestRelease"]["version"]
            date = data['0']["last_two_releases"]["LatestRelease"]["date"]
            md_title = [
                "Repository name: {}\n Current version: {} released on {}".format(repository_name, version, date)]

        except:
            md_title = ["{} commit markdown table since {}".format(repository_name, lastWeek)]
        commit_number_list = [key for key in data]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            commit_number = commit_number_list[-1]
            if int(key) < 2000:
                try:
                    commit_author = data[key]["commiter_name"]
                    commit_author = re.sub("\u0131", "i", commit_author)  # this is temporary
                    commit_author = re.sub("\x94", "\"", commit_author)

                    date = data[key]["commit_date"]

                    message = data[key]["commit_message"]
                    message = re.sub("\|", "\|", message)
                    message = re.sub("\x94", "\"", message)
                    # Used for debugging
                    print("[" + key + "]" + message)

                    url = data[key]["url"]

                    row = "|" + commit_number + \
                          "|" + commit_author + \
                          "|" + message + \
                          "|" + "[URL](" + url + ")" + \
                          "|" + date + "\n"

                    del commit_number_list[-1]
                    for repo in tables.keys():
                        tables[repo] = tables[repo] + row
                except KeyError:
                    pass

        md_file_name = "{}.md".format(repository_name)
        md_file = open(current_dir + "/{}/".format(path_to_files) + md_file_name, "w")

        try:
            for key, value in tables.items():
                if value != base_table:
                    md_file.write("## " + key.upper() + "\n\n")
                    md_file.write(value + "\n\n")
        except KeyError:
            pass

        md_file.close()
    except FileNotFoundError:
        print("Json for {} is empty! Skipping!".format(repository_name))


def clear_file(file_name, string_number_of_commits="five"):
    """
    This function takes a file that clears the content and output's a base table header for a markdown file.
    :param string_number_of_commits: literal number that needs to match the number of commits shown on main markdown
    table
    :param file_name: Name of the file to be written. (should also contain the path)
    :return: A file should be created and should contain base table.
    """
    file = open(file_name, "w")
    heading = "#  Last " + string_number_of_commits + " commits from every repository \n"
    file.write(heading)
    file.close()


def generate_main_md_table(path_to_files):
    """
    Looks into repositories folders (hg_files & git files), filters the files to load the json's using a passfilter and
    calls after extraction functions.
    :param path_to_files: Folder to json files
    """
    # Get current folder path.
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Look into repositories folder and list all of the files
    only_files = [f for f in listdir(dir_path + "/{}".format(path_to_files)) if
                  isfile(join(dir_path + "/{}".format(path_to_files), f))]

    # Pass filter only the ".json" objects
    json_files = [jf for jf in only_files if ".json" in jf]

    # Extract data from json_files and writes to main markdown table.
    extract_json(json_files, path_to_files)

    print("Table successfully generated.")


def extract_json(json_files, path_to_files, commits_per_repo=5):
    """
    Extracts the json data from json files and writes the data to the main markdown table file. The function looks
    into json files after the last commit, extracts it and calls the write_main_md_table function.
    :param commits_per_repo: number of commits to be used in the main markdown file
    :param json_files: List of files to extract commits from.
    :param path_to_files: Folder to json files
    :return: none
    """
    for file in json_files:
        file_path = "{}/".format(path_to_files) + file

        with open(file_path) as json_files:
            data = json.load(json_files)
            base_link = "https://github.com/Akhliskun/firefox-infra-changelog/blob/master/{}/".format(path_to_files)
            repository_url = base_link + file.rstrip().replace(" ", "%20").rstrip().replace(".json", ".md")
            repository_json = base_link + file.rstrip().replace(" ", "%20")
            repository_title = file.replace(".json", "")
            try:
                # Generates the markdown header for a specific repository
                generate_markdown_header("main_md_table.md", repository_title, repository_url, repository_json)
                # Write the commits from json files into the main markdown table
                # The number of commits writen to a table depends on the commits_per_repo value (by default = 5 in the
                # function definition.
                for commit_iterator in range(1, commits_per_repo + 1):
                    # The commit number must be a number with string type.
                    commit_number = str(commit_iterator)
                    commit_description = data[commit_number]["commit_message"]
                    commit_url = data[commit_number]["url"]
                    repository_url = "[Link to commit](" + commit_url + ")"
                    commit_date = data[commit_number]["commit_date"]
                    write_main_md_table("main_md_table.md", repository_url, commit_description, commit_date)

            except KeyError:
                print("File " + file + " is empty. \n Please check:" + repository_url + " for more details.\n")
                pass


def generate_markdown_header(file_name, repository_name, markdown_link, json_link):
    """
    This function appends the markdown header to the main markdown table. It includes the repository title (name), the
    markdown link and the json link.
    :param file_name: name of the file in which the content it's added.
    :param repository_name: name of the repository for the generated table.
    :param markdown_link: markdown link for the header table.
    :param json_link: json link for the header table.
    :return: none, expected to write to file_name.
    """
    file = open(file_name, "a")

    repository_title = "|\t" + repository_name + "\t|\t" + "[MarkDown](" + markdown_link + ")" + "\t|\t" + "[Json](" + \
                       json_link + ")" + "\t| \n"
    title_table_formation = "|:----------------:|:-------------------------------------:|:----------" \
                            "-----------------------:| \n "
    base_table = "|      Repository      |                   Last commit               |    Deploy time       | \n" + \
                 "|:--------------------:|:-------------------------------------------:|:--------------------:| \n"
    file.write("\n" + repository_title + title_table_formation + "\n" + base_table)
    file.close()


def write_main_md_table(file_name, repository_url, last_commit, deploy_time):
    """
    This function opens a file (that file should be already created and appends to it a row that will contain the
    repository, the last commit and the deploy time.
    :param file_name: Name of the file in which the content is appended. (should also contain the path)
    :param repository_url: Repository url for the first element of the table.
    :param last_commit: Description of the last commit used as the 2nd element of the table
    :param deploy_time: Time and Time designator used as the 3rd element of the table
    :return:
    """
    row = "|" + repository_url + \
          "|" + last_commit + \
          "|" + deploy_time + \
          "|" + "\n"
    write_file = open(file_name, "a")
    write_file.write(row)


if __name__ == "__main__":
    TOKEN = os.environ.get("GIT_TOKEN")
    git = Github(TOKEN)
    repositories_data = open("./repositories.json").read()
    repositories = json.loads(repositories_data)
    create_files_for_git(repositories)
    create_files_for_hg(repositories)
    clear_file("main_md_table.md")
    generate_main_md_table("hg_files")
    generate_main_md_table("git_files")