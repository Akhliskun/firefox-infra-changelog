import requests
import json
import re

reposLIST = {'ship-it': 'https://api.github.com/repos/mozilla-releng/ship-it/commits',
            'release-services': 'https://api.github.com/repos/mozilla/release-services/commits',
            'beetmoverscript': 'https://api.github.com/repos/mozilla-releng/beetmoverscript/commits',
            'addonscript': 'https://api.github.com/repos/mozilla-releng/addonscript/commits',
            'shipit-v2': 'https://api.github.com/repos/mozilla-releng/shipit-v2/commits',
            'build-cloud-tools': 'https://api.github.com/repos/mozilla-releng/build-cloud-tools/commits',
            'build-puppet': 'https://api.github.com/repos/mozilla-releng/build-puppet/commits',
            'shipitscript': 'https://api.github.com/repos/mozilla-releng/shipitscript/commits',
            'bouncerscript': 'https://api.github.com/repos/mozilla-releng/bouncerscript/commits',
            'treescript': 'https://api.github.com/repos/mozilla-releng/treescript/commits',
            'mozapkpublisher': 'https://api.github.com/repos/mozilla-releng/mozapkpublisher/commits',
            'OpenCloudConfig': 'https://api.github.com/repos/mozilla-releng/OpenCloudConfig/commits',
            'scriptworker': 'https://api.github.com/repos/mozilla-releng/scriptworker/commits',
            'pushsnapscript': 'https://api.github.com/repos/mozilla-releng/pushsnapscript/commits',
            'signingscript': 'https://api.github.com/repos/mozilla-releng/signingscript/commits',
            'cot-gpg-keys': 'https://api.github.com/repos/mozilla-releng/cot-gpg-keys/commits',
            'pushapkscript': 'https://api.github.com/repos/mozilla-releng/pushapkscript/commits',
            'balrogscript': 'https://api.github.com/repos/mozilla-releng/balrogscript/commits',
            'funsize': 'https://api.github.com/repos/mozilla-releng/funsize/commits',
            'signtool': 'https://api.github.com/repos/mozilla-releng/signtool/commits'
}

char_list = ['api.', '/repos', '/commits'] #list for strings we dont want in the repo link
for reposLIST_key, reposLIST_value in reposLIST.items():     # for loop to scroll through the reposLIST
    url = re.sub("|".join(char_list), "", reposLIST_value) # this actually removes strings from char_list to generate basic
    r = requests.get(reposLIST.get(reposLIST_key))     # get infos from gitAPI
    p = r.json()     # turn into JSON content
    commit = {}  # dictionary with key = SHA and values=name, email, date, URL and message
    commit_number = 0
    for keys in p:    # loop to scroll through json content
        author = {}    # dictionary with info about commiter and commit
        commit_message = keys['commit']['message']
        message = re.sub('[*\n\r]', ' ', commit_message) # removes "\n" "\r" from commit messages. Such characters create bugs in github_changelog.json
        author.update({ 'Name': keys['commit']['author']['name'],
                        'Email': keys['commit']['author']['email'],
                        'Date': keys['commit']['author']['date'],
                        'URL Commit': keys['commit']['url'],
                        'Message': message,
                        'Url Repo': url})     # add info in author dictionary
        commit.update({commit_number: author})
        commit_number += 1
    reposLIST.update({reposLIST_key : commit})     # add all the info into the main dictionary
with open('./github_changelog.json', 'w') as fp:     # open .json file with write permission
    json.dump(reposLIST, fp)     # write in the .json file as a string



''' Using this Json viewer " http://www.jsonviewer.com/ ",
        you can copy the content from github_changelog.json into RAW json data:
            and see all the commits '''