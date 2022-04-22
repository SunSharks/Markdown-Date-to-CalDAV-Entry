import os
import markdown
from datetime import datetime
from pw import search_path, get_last_run, set_last_run
set_last_run()


class search_remindmes:
    def __init__(self, search_whole_dir=False):
        self.lastrun = datetime(2022, 4, 22, 1, 1, 1)  # get_last_run()
        self.searchables = {}
        self.search_whole_dir = search_whole_dir

    def get_last_edit_date(self, file="ical.py"):
        lastmodified = os.stat(file).st_mtime
        # print(datetime.fromtimestamp(lastmodified).hour)
        return datetime.fromtimestamp(lastmodified)

    def walk(self):
        for path, subdirs, files in os.walk(search_path):
            for name in files:
                full_path = os.path.join(path, name)
                if self.get_last_edit_date(full_path) > self.lastrun or self.search_whole_dir:
                    if full_path.endswith(".md"):
                        self.searchables[full_path] = self.search_file_for_remindme(full_path)
        return

    def search_file_for_remindme(self, file):
        with open(file, 'r') as f:
            self.cmdstr = markdown.markdown(f.read())

        cmdlst = self.cmdstr.split("\n")
        mdcmd_found = False
        mdstr = ""
        for cmd in cmdlst:
            if "~ REMINDME" in cmd or mdcmd_found:
                mdstr += cmd + "\n"
                mdcmd_found = True
            if "**~**" in cmd and mdcmd_found:
                mdcmd_found = False
        return mdstr
    #


search_remindmes()
# print(os.listdir(search_path))
