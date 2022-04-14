import os
from datetime import datetime
from pw import search_path, last_run


def get_last_edit_date(file="ical.py"):
    lastmodified = os.stat(file).st_mtime
    # print(datetime.fromtimestamp(lastmodified).hour)
    return datetime.fromtimestamp(lastmodified)


#
get_last_edit_date()
print("hai")
for path, subdirs, files in os.walk(search_path):
    for name in files:
        full_path = os.path.join(path, name)
        print(name)
        if get_last_edit_date(full_path) < last_run:
            with open(full_path, 'r') as f:
                l = f.readlines()
                print(l)
                break

# print(os.listdir(search_path))
