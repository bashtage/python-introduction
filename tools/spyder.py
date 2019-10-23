import nbconvert


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

