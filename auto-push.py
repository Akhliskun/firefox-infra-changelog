import os
import requests
import subprocess
import base64
from fic_modules.configuration import (
    REPO_LIST,
    REPOSITORIES,
    GIT
)
from fic_modules.helper_functions import get_keys

repo = GIT.get_repo("mozilla-releng/firefox-infra-changelog")
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def update_git(name, folder):
    """
    :param name: name of the repository
    :param folder: git_files/hg_files depending where the repo is hosted
    :return:
    """
    file_content = get_content(name, folder)
    file_encode = base64.b64encode(bytes(file_content, "utf8"))
    file_decode = base64.b64decode(str(file_encode, "utf-8"))
    content = repo.get_contents("{}/{}.json".format(folder, name))
    repo.update_file(content.path, "Update files", file_decode, content.sha, branch="TestPush")


def update_hg(name, folder):
    """
    :param name: name of the repository
    :param folder: git_files/hg_files depending where the repo is hosted
    :return:
    """
    filename = "{}.json".format(name)
    file_content = get_content(name, folder)
    file_encode = base64.b64encode(bytes(file_content, "utf8"))
    file_decode = base64.b64decode(str(file_encode, "utf-8"))
    sha_request = requests.get('https://api.github.com/repos/mozilla-releng/firefox-infra-changelog/git/trees/master').json()
    for key in sha_request.get('tree'):
        if key.get('path') == 'hg_files':
            hg_files_sha = key.get('sha')
            hg_files_request = requests.get(
                'https://api.github.com/repos/mozilla-releng/firefox-infra-changelog/git/trees/{}'.format(hg_files_sha)).json()
            for key in hg_files_request.get('tree'):
                if key.get('path') == filename:
                    sha = key.get('sha')
                    repo.update_file("hg_files/{}.json".format(name), "Update files", file_decode,
                             sha, branch="TestPush")


def get_content(repository_name, repo_type):
    """
    :param repository_name: repository name
    :param new_commits: git_files/hg_files depending where the repo is hosted
    :return: content of .json file
    """
    json_filename = "{}.json".format(repository_name)
    try:
        with open(CURRENT_DIR + "./{}/".format(repo_type) + json_filename, "r",newline="\n") as \
                commit_json:
            json_content = commit_json.read()
    except FileNotFoundError:
        json_content = ""
    return json_content


subprocess.call(['git', 'checkout', 'master'])
subprocess.call(['git', 'pull'])
subprocess.call(['python', 'client.py', '-c', '-l'])
get_keys("Github")
get_keys("Mercurial")
for repository in REPO_LIST:
    if repository in REPOSITORIES.get("Github"):
        update_git(repository, "git_files")
    elif repository in REPOSITORIES.get("Mercurial"):
        update_hg(repository, "hg_files")
