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

spyder_dir = os.path.join("..", "course", "autumn", "spyder")
if not os.path.exists(spyder_dir):
    os.mkdir(spyder_dir)

source_dir = "../solutions/autumn/"
nb_files = glob.glob(os.path.join(source_dir, "*.ipynb"))

# Ensure data-dataset-construction is run first so that data is available
for nb_file in nb_files:
    if "construction" in nb_file:
        first = nb_file
nb_files.remove(first)
nb_files.insert(0, first)

for nb_file in nb_files:
    print(f"Processing {nb_file}")
    nb = nbformat.read(nb_file, 4)
    executed = pre.execute.executenb(nb, cwd=source_dir, kernel_name="python3")
    print(f"Writing executed version of {nb_file}")
    nbformat.write(executed, nb_file, nbformat.NO_CONVERT)
    cop = pre.ClearOutputPreprocessor()
    nb, _ = cop.preprocess(executed, {})

    for cell in nb["cells"]:
        if isinstance(cell, MutableMapping):
            if (
                "cell_type" not in cell
                or cell["cell_type"] != "code"
                or "# Setup" in cell["source"]
            ):
                continue
            cell["source"] = ""
            if "metadata" in cell and "pycharm" in cell["metadata"]:
                del cell["metadata"]["pycharm"]
    _, base = os.path.split(nb_file)
    out = os.path.abspath(os.path.join("..", "course", "autumn", base))
    print(f"Writing clean version to {out}")
    nbformat.write(nb, out, nbformat.NO_CONVERT)

    # Export for Spyder
    code = export_for_spyder(copy.deepcopy(nb))
    py_name = os.path.split(nb_file)[-1].replace(".ipynb", ".py")
    with open(os.path.join(spyder_dir, py_name), "w", encoding="utf8") as python_file:
        python_file.write(code)
