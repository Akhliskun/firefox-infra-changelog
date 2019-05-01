from fic_modules.GITMethods import FICGithub
import subprocess
from fic_modules.configuration import LOGGER
from datetime import datetime

config = "."
commit_message = "Changelog: " + str(datetime.utcnow())
files = ["git_files", "hg_files", "changelog.json", "changelog.md"]

update_fic_files = FICGithub(files, commit_message, LOGGER, config)

update_fic_files.git_pull()
subprocess.call(['python', 'client.py', '-a', '-l'])
update_fic_files.git_add()
update_fic_files.git_commit()
update_fic_files.git_push()

