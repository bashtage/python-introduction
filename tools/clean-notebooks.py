"""
Execute and then clear code and output from solutions notebooks.
"""
import asyncio
import copy
import glob
import os
import sys
from collections.abc import MutableMapping

import black.mode as bm
import nbclient
import nbconvert.preprocessors as pre
import nbformat
from latex import key
from spyder import export_for_spyder


# See https://bugs.python.org/issue37373 :(
if (
    sys.version_info[0] == 3
    and sys.version_info[1] >= 8
    and sys.platform.startswith("win")
):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

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
    executed = nbclient.execute(nb, cwd=source_dir, kernel_name="python3")
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
executed = nbclient.execute(nb, cwd=source_dir, kernel_name="python3")
cop = pre.ClearOutputPreprocessor()
nb, _ = cop.preprocess(executed, {})
for cell in nb["cells"]:
    if isinstance(cell, MutableMapping):
        if "metadata" in cell and "pycharm" in cell["metadata"]:
            del cell["metadata"]["pycharm"]

code = export_for_spyder(nb)
with open(os.path.join(spyder_dir, "demo.py"), "w", encoding="utf8") as python_file:
    python_file.write(code)
