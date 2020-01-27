"""
Execute and then clear code and output from solutions notebooks.
"""
import copy
import glob
import json
import os
from hashlib import sha512

import nbconvert.preprocessors as pre
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from spyder import export_for_spyder

if os.path.exists("course-hashes.json"):
    with open("course-hashes.json", "r") as hash_file:
        hashes = json.load(hash_file)
else:
    hashes = {}

terms = ("autumn", "winter")

for term in terms:
    spyder_dir = os.path.join("..", "course", term, "spyder")
    os.makedirs(spyder_dir, exist_ok=True)

nb_files = []
for term in terms:
    source_dir = os.path.join("../solutions/" + term)
    files = glob.glob(os.path.join(source_dir, "*.ipynb"))
    nb_files.extend(files)

# Ensure data-dataset-construction is run first so that data is available
first = []
for nb_file in nb_files:
    if "construction" in nb_file:
        first.append(nb_file)
if first:
    for nb in first:
        nb_files.remove(nb)
        nb_files.insert(0, nb)

for nb_file in nb_files:
    print(f"Processing {nb_file}")
    nb = nbformat.read(nb_file, 4)
    term = "autumn" if "autumn" in nb_file else "winter"
    source_dir = os.path.join("../solutions/" + term)
    spyder_dir = os.path.join("..", "course", term, "spyder")
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    nb_hash = "" if nb_file not in hashes else hashes[nb_file]

    cell_source = ""
    for cell in nb["cells"]:
        source = "" if "source" not in cell else cell["source"]
        cell_source += source.strip()
    current = sha512(cell_source.encode("utf-8")).hexdigest()
    nb_changed = current != nb_hash
    if nb_changed:
        ep.preprocess(nb, {'metadata': {'path': source_dir}})
        print(f"Writing executed version of {nb_file}")
        nbformat.write(nb, nb_file, nbformat.NO_CONVERT)
        hashes[nb_file] = current
    cop = pre.ClearOutputPreprocessor()
    nb, _ = cop.preprocess(nb, {})
    retain = []
    for cell in nb["cells"]:
        cell_type = cell.get("cell_type", None)
        source = cell.get("source", "")
        if cell_type == "markdown" and "### Explanation" in source:
            continue
        if cell_type == "code" and "# Setup" not in cell["source"]:
            cell["source"] = ""
        if "metadata" in cell and "pycharm" in cell["metadata"]:
            del cell["metadata"]["pycharm"]
        retain.append(cell)
    # Filter repeated empty cells
    keep = []
    for i, cell in enumerate(reversed(retain)):
        cell_type = cell.get("cell_type", None)
        if cell_type != "code":
            keep.append(len(retain)-i-1)
            continue
        if len(retain)-i-2 < 0:
            break
        if cell["source"].strip() != "":
            keep.append(len(retain)-i-1)
            continue
        prev_cell = retain[len(retain)-i-2]
        prev_cell_type = prev_cell.get("cell_type", None)
        if prev_cell_type != cell_type:
            keep.append(len(retain)-i-1)
    keep = sorted(keep)
    retain = [retain[i] for i in keep]

    nb["cells"] = retain

    _, base = os.path.split(nb_file)
    out = os.path.abspath(os.path.join("..", "course", term, base))
    print(f"Writing clean version to {out}")
    nbformat.write(nb, out, nbformat.NO_CONVERT)

    # Export for Spyder
    code = export_for_spyder(copy.deepcopy(nb))
    py_name = os.path.split(nb_file)[-1].replace(".ipynb", ".py")
    with open(os.path.join(spyder_dir, py_name), "w", encoding="utf8") as python_file:
        python_file.write(code)

with open("course-hashes.json", "w") as hash_file:
    json.dump(hashes, hash_file)
