import os
import json
import markdown2

current_dir = os.path.dirname(os.path.realpath(__file__))

json_data= open('./github_changelog.json').read()
data = json.loads(json_data)

repos = ['shipit']

base_table = "| Commit Number | Message | Data | \n" + \
            "|:---:|:----------------------------------:|:----:| \n"
tables = {}
for repo in repos:
    tables[repo] = base_table

categories = data['shipit']


for key, value in categories.items():
    ncommit = key
    lastMsg = categories[key]['Message: ']
    date = categories[key]["Date: "]

    row = "|" + ncommit +\
        "|" + lastMsg +\
        "|" + date + '\n'
    print(row)
    for repo in ncommit:
        for repos in tables:
            print (tables[repos])
            tables[repos] = tables[repos] + row

#print (tables.items())
output_files = []
md_file_name = "It's shipit!.md"
md_file = open(current_dir + "/../" + md_file_name, 'w')

for key, value in tables.items():
    if value != base_table:
        md_file.write("## " + key.upper() + "\n\n")
        md_file.write(value + "\n\n")
        html_file_name = key.replace(" ", "_") + ".html"
        html_file = open(current_dir + "/../" + html_file_name, "w")
        html_table = markdown2.markdown(value.encode('utf8'), extras=["tables"])
        html_file.write(html_table)
        html_file.close()
        output_files.append(html_file_name)
md_file.close()
output_files.append(md_file_name)
