"""
Rename notebooks if lesson numbers are not numeric
"""

import glob
import subprocess

RENAME = True

files = glob.glob("../solutions/introduction/lesson-*.ipynb")
notebooks = {}
need_rename = False
for nb in files:
    key = nb.split("-")[-1].replace(".ipynb", "")
    alpha_numeric = False
    try:
        int(key)
    except ValueError:
        alpha_numeric = True
        need_rename = True

    if len(key) == 1 or (alpha_numeric and len(key) == 2):
        key = "0" + key
    notebooks[key] = nb

if need_rename and RENAME:
    num_nb = len(notebooks)
    for i, key in enumerate(reversed(sorted(notebooks.keys()))):
        new_number = num_nb - i
        new_name = f"lesson-{new_number}"
        nb_file = notebooks[key]
        new_file_name = nb_file.split("-")[0]
        new_file_name = f"{new_file_name}-{new_number}.ipynb"
        import os

        src = os.path.abspath(notebooks[key])
        dest = os.path.abspath(new_file_name)
        if src != dest:
            subprocess.call(["git", "mv", src, dest])
