import os
import glob

files = glob.glob('../solutions/lesson-*.ipynb')
notebooks = {}
for nb in files:
    key = nb.split('-')[-1].replace('.ipynb', '')
    alpha_numeric = False
    try:
        int(key)
    except ValueError:
        alpha_numeric = True

    if len(key) == 1 or (alpha_numeric and len(key)==2):
        key = '0' + key
    notebooks[key] = nb


num_nb = len(notebooks)
for i, key in enumerate(reversed(sorted(notebooks.keys()))):
    new_number = num_nb - i
    new_name = f'lesson-{new_number}'
    print(notebooks[key], new_name)



#num_nb = len(notebooks)
#for i, nb in enumerate(reversed(notebooks)):
