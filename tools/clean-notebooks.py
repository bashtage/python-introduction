"""
Execute and then clear code and output from solutions notebooks.
"""
from collections.abc import MutableMapping
import copy
import glob
import os

import nbconvert
import nbconvert.preprocessors as pre
import nbformat

from latex import key


def export_for_spyder(nb):
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] in ("markdown", "code"):
            cell["source"] = "#%%\n" + cell["source"]

    exporter = nbconvert.PythonExporter()
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    exporter.exclude_output = True
    py = exporter.from_notebook_node(nb)

    code = py[0].split("\n")
    code = [line if line != "# #%%" else "#%%" for line in code]
    imported_get_python = False
    for i, line in enumerate(code):
        if line.startswith("get_ipython()") and not imported_get_python:
            code.insert(i, "from IPython import get_ipython")
            imported_get_python = True
    return "\n".join(code)


website_dir = os.path.join("..", "website")
if not os.path.exists(website_dir):
    os.mkdir(website_dir)
spyder_dir = os.path.join("..", "course", "introduction", "spyder")
if not os.path.exists(spyder_dir):
    os.mkdir(spyder_dir)

source_dir = "../solutions/introduction/"
nb_files = glob.glob(os.path.join(source_dir, "*.ipynb"))
nb_files = sorted(nb_files, key=lambda v: key(v))

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
    out = os.path.abspath(os.path.join("..", "course", "introduction", base))
    print(f"Writing clean version to {out}")
    nbformat.write(nb, out, nbformat.NO_CONVERT)

    # Export for Spyder
    code = export_for_spyder(copy.deepcopy(nb))
    py_name = os.path.split(nb_file)[-1].replace(".ipynb", ".py")
    with open(os.path.join(spyder_dir, py_name), "w", encoding="utf8") as python_file:
        python_file.write(code)

    # Prepare for website
    slug, _ = os.path.splitext(base)
    title = slug.capitalize().replace("-", " ")
    nikola = {
        "category": "teaching",
        "date": "2019-09-04 17:18:32 UTC+01:00",
        "description": "",
        "link": "",
        "slug": slug,
        "tags": "",
        "title": title,
        "type": "text",
    }
    nb["metadata"]["nikola"] = nikola
    for cell in nb["cells"]:
        if isinstance(cell, MutableMapping) and cell["cell_type"] == "markdown":
            source = cell["source"]
            source = source.replace("(images/", "(/images/teaching/python/course/")
            cell["source"] = source
    out = os.path.abspath(os.path.join(website_dir, base))
    print(f"Writing website version to {out}")
    nbformat.write(nb, out, nbformat.NO_CONVERT)

print("Exporting demo to python")
demo = "../course/introduction/demo.ipynb"
nb = nbformat.read(demo, 4)
# Verify that it executes
executed = pre.execute.executenb(nb, cwd=source_dir, kernel_name="python3")
cop = pre.ClearOutputPreprocessor()
nb, _ = cop.preprocess(executed, {})
for cell in nb["cells"]:
    if isinstance(cell, MutableMapping):
        if "metadata" in cell and "pycharm" in cell["metadata"]:
            del cell["metadata"]["pycharm"]

code = export_for_spyder(nb)
with open(os.path.join(spyder_dir, "demo.py"), "w", encoding="utf8") as python_file:
    python_file.write(code)
