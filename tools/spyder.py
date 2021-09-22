import asyncio
import sys

import isort
import black
import black.mode as bm
import nbconvert

# See https://bugs.python.org/issue37373 :(
if (
    sys.version_info[0] == 3
    and sys.version_info[1] >= 8
    and sys.platform.startswith("win")
):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


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
    mode = bm.Mode([bm.TargetVersion.PY38, bm.TargetVersion.PY39])
    code = black.format_file_contents("\n".join(code), mode=mode, fast=False)
    code = isort.api.sort_code_string(code)

    return code
