"""
Execute and then clear code and output from solutions notebooks.
"""
from collections.abc import MutableMapping
import copy
import glob
import os

import nbconvert.preprocessors as pre
import nbformat

from spyder import export_for_spyder

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

nb_files = nb_files[-1:]
for nb_file in nb_files:
    print(f"Processing {nb_file}")
    nb = nbformat.read(nb_file, 4)
    term = "autumn" if "autumn" in nb_file else "winter"
    source_dir = os.path.join("../solutions/" + term)
    spyder_dir = os.path.join("..", "course", term, "spyder")
    executed = pre.execute.executenb(nb, cwd=source_dir, kernel_name="python3")
    print(f"Writing executed version of {nb_file}")
    nbformat.write(executed, nb_file, nbformat.NO_CONVERT)
    cop = pre.ClearOutputPreprocessor()
    nb, _ = cop.preprocess(executed, {})
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
