import os
import json
import markdown2

current_dir = os.path.dirname(os.path.realpath(__file__))

json_data= open('./github_changelog.json').read()
data = json.loads(json_data)

repos = ['shipit',
'services',
'beetmoverscript',
'addonscript',
'shipitv2',
'build-cloud-tools',
'build-puppet',
'shipitscript',
'bouncerscript',
'treescript',
'mozapkpublisher',
'OpenCloudConfig',
'scriptworker',
'pushsnapscript',
'signingscript',
'cot-gpg-keys',
'pushapkscript',
'balrogscript',
'funsize',
'signtool']

base_table = "| Repo | Last Commit Msg | Date |\n" +\
             "| :-------------------------------------: |:----------------------:| :----: |\n"

tables = {}

for repo in repos:
    tables[repo] = base_table

for key in data:
    for keys in data[key]:
        categories = key
        lastMsg = data[key][keys]['Message: ']
        date = data[key][keys]["Date: "]
    #print (lastMsg)

        row = "|" + categories +\
        "|" + lastMsg +\
        "|" + date + '\n'
        for repo in categories:
            for repo in tables:
                tables[repo] = tables[repo] + row
            #print (tables[repo])
#print (tables.items())
output_files = []
md_file_name = "OutStandingProjects.md"
md_file = open(current_dir + "/../" + md_file_name, 'w')

for cheie, valoare in tables.items():
    if valoare != base_table:

        md_file.write("## " + cheie.upper() + "\n\n")
        md_file.write(valoare + "\n\n")

        html_file_name = cheie.replace(" ", "_") + ".html"
        html_file = open(current_dir + "/../" + html_file_name, "w")
        html_table = markdown2.markdown(valoare.encode('utf8'), extras=["tables"])
        html_file.write(html_table)
        html_file.close()
        output_files.append(html_file_name)

md_file.close()
output_files.append(md_file_name)
