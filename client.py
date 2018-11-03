import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta
import requests
import json

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


def create_git_link(project):
    """
    Expects the name of a project as a parameter and creates the api link for the json.
    We know 'services' is the only project in the mozilla repo while the rest are in mozilla-releng
    :param project:
    :return: GitHub Api link
    """
    beginning_url = "https://api.github.com/repos/"
    end_url = "/commits"
    if project == "release-services":
        git_url = beginning_url + "mozilla/" + project + end_url
    else:
        git_url = beginning_url + "mozilla-releng/" + project + end_url
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
    :param commit_data:
    :return: filtered json data
    """
    repo_dict = {}
    number = 1
    for item in commit:
        each_commit = {}
        author_info = {}
        author_info.update({'sha': item['sha'],
                            'url': item['url'],
                            'author_info': item['commit']['author'],
                            'commit_message': item['commit']['message']})
        each_commit.update({number: author_info})
        number += 1
        repo_dict.update(each_commit)
    return repo_dict


if __name__ == "__main__":
    user = git.get_user()  # Get Name of user.
    print(user.name + " is asking: ")
    project = input("What to search? : ")
    commit_data = get_commits(create_git_link(str(project)))
    useful_data = filter_commit_data(commit_data)
    write_commits(useful_data, "changelog.json")
    create_md_table(project)
