import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta
import requests
import json
import re

# Create a Github instance:
TOKEN = os.environ.get("GIT_TOKEN")
git = Github(TOKEN)


def create_md_table(project):
    """
    Uses 'project' parameter to generate markdown table.
    :param project:
    :return:
    """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    json_data = open('./changelog.json').read()
    data = json.loads(json_data)
    base_table = "| Commit Number | Commiter | Commit Message | Date | \n" + \
                 "|:---:|:----:|:----------------------------------:|:----:| \n"
    tables = {}
    md_title = ['{} markdown table'.format(project)]
    for repo in md_title:
        tables[repo] = base_table

    for key in data:
        commit_number = key
        commiter = data[key]["author_info"]["name"]
        date = data[key]["author_info"]["date"]
        message = data[key]["commit_message"]

        row = "|" + commit_number + \
              "|" + commiter + \
              "|" + message + \
              "|" + date + '\n'

        for repo in tables.keys():
            tables[repo] = tables[repo] + row

    md_file_name = "{}.md".format(project)
    md_file = open(current_dir + "/repositories/" + md_file_name, 'w')

    for key, value in tables.items():
        if value != base_table:
            md_file.write("## " + key.upper() + "\n\n")
            md_file.write(value + "\n\n")

    md_file.close()


def hg_timestamps_handler(timestamp, timezone):
    """
    This function handles the mercurial timestamps so that all of the modifications to be traceable in time, in
    concordance to one
    another and returns the date-time format.
    Part of Mercurial Wrapper
    Example :
        print(handle_timestamps("1499225169.0", "-43200"))
    Output:
        07-05-2017 15:26:09
    :param timestamp: Timestamp in unix systems (an unique time represented in how many seconds past a certain event)
    :param timezone: Timezone of the timestamp
    :return: Returns "YYYY-MM-DD HH:MM:SS"
    """
    if "-" in timezone:
        ts = int(timestamp[:-2]) - int(timezone)
    else:
        ts = int(timestamp[:-2]) + int(timezone)
    return datetime.utcfromtimestamp(ts).strftime("%m-%d-%Y %H:%M:%S")


def get_hg_changes(repository_name, push_type):
    """
    This function takes a repository and push type and returns a json object that contains changes in that specific
    repository.
    The HG API also supports xml and rss.

    Example:
    example = get_push("https://hg.mozilla.org/build/nagios-tools/", "json-log")
    This will be later used to get the commits from https://hg.mozilla.org/

    :param repository_name: link of the repository, eg: https://hg.mozilla.org/build/nagios-tools/
    :param push_type: would probably be "json-log" most of the time.
    :return:
    """
    if push_type == "json-log":
        request_url = repository_name + push_type
        push_response = requests.get(request_url)
        hg_changes_result = push_response.json()
    else:
        print("Feature not implemented. Please use \"json-log\".")
    return hg_changes_result


def create_git_link(team, project):
    """
    Expects the name of a project as a parameter and creates the api link for the json.
    We know 'services' is the only project in the mozilla repo while the rest are in mozilla-releng
    :param project:
    :return: GitHub Api link
    """
    beginning_url = "https://api.github.com/repos/"
    end_url = "/commits"
    git_url = beginning_url + team + project + end_url
    return git_url


def get_commits(link):
    """
    Makes the json request and return the request result as a list.
    :param link:
    :return: json list
    """
    commits_response = requests.get(link)
    commits_result = commits_response.json()
    return commits_result


def write_commits(commit_content, file_name):
    """
    Writes commit content to a provided file.
    :param commit_content:
    :param file_name:
    :return: none
    """
    with open(file_name, "w") as json_file:
        json.dump(commit_content, json_file, indent=2)


def filter_commit_data(commit):
    """
    Filters out only the data that we need from a commit
    :param commit:
    Substitute the special characters from commit message using 'sub' function from 're' library
    :param commit:
    :return: filtered json data
    """
    repo_dict = {}
    number = 0
    for item in commit:
        each_commit = {}
        author_info = {}
        commit_message = item['commit']['message']
        message = re.sub('[*\n\r]', ' ', commit_message)
        author_info.update({'sha': item['sha'],
                            'url': item['url'],
                            'author_info': item['commit']['author'],
                            'commit_message': message})
        each_commit.update({number: author_info})
        number += 1
        repo_dict.update(each_commit)
    return repo_dict


if __name__ == "__main__":
    repositories_data = open('./repositories.json').read()
    repositories = json.loads(repositories_data)

    # Github
    """
    Goes through every repo under github and creates a separate MD file for each one
    """
    for repo in repositories["Github"]:
        repository_name = repositories["Github"][repo]["name"]
        repository_team = repositories["Github"][repo]["team"]
        git_link = create_git_link(repository_team, repository_name)
        commit_data = get_commits(git_link)
        useful_data = filter_commit_data(commit_data)
        write_commits(useful_data, "changelog.json")
        create_md_table(repository_name)
    # Mercurial
    """
    Goes through every repo under mercurial and creates a separate MD file for each one
    """
    for repo in repositories["Mercurial"]:
        repository_url = repositories["Mercurial"][repo]["url"]
        repository_push_type = repositories["Mercurial"][repo]["configuration"]["push_type"]
        repository_name = repositories["Mercurial"][repo]["name"]
        hg_changes = get_hg_changes(repository_url, repository_push_type)
        hg_json_name = "./repositories/" + "{}.json".format(repository_name)
        write_commits(hg_changes, hg_json_name)
