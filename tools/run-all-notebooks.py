import glob
import os
from asyncio import WindowsSelectorEventLoopPolicy, set_event_loop_policy

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

set_event_loop_policy(WindowsSelectorEventLoopPolicy())

CUR_DIR = os.path.split(os.path.abspath(__file__))[0]
BASE_DIR = os.path.abspath(os.path.join(CUR_DIR, "..", "solutions"))
INTRO_NB = glob.glob(os.path.join(BASE_DIR, "introduction", "*.ipynb"))
AUTUMN_NB = glob.glob(os.path.join(BASE_DIR, "autumn", "*.ipynb"))
WINTER_NB = glob.glob(os.path.join(BASE_DIR, "winter", "*.ipynb"))

AUTUMN_ORDER = ["data", "estimation", "regression", "arma"]
WINTER_ORDER = ["arch", "value", "vector"]
INTRO_NB = [f for f in sorted(INTRO_NB) if not ("final" in f or "installation" in f)]

final = INTRO_NB[:]
for name in AUTUMN_ORDER:
    final.extend(sorted([f for f in AUTUMN_NB if name in f]))
for name in WINTER_ORDER:
    final.extend(sorted([f for f in WINTER_NB if name in f]))
final = [f for f in final if not f.endswith("executed.ipynb")]
# Reorder VaR notebooks
to_reorder = [nb for nb in final if "value-at-risk-forecast-evaluation.ipynb" in nb]
final.remove(to_reorder[0])
for i, val in enumerate(final):
    if val.startswith("vector"):
        break
final.insert(i, to_reorder[0])

for notebook_filename in final:
    out = notebook_filename.replace(".ipynb", "-executed.ipynb")
    if os.path.exists(out):
        print(f"Skipping {notebook_filename}")
        continue
    print(f"Reading {notebook_filename}")
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)
    path = os.path.split(notebook_filename)[0]
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": path + "/"}})

    print(f"Writing {out}")
    with open(out, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
