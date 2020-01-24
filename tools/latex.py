"""
Tools for manipulating the LaTeX produced from notebooks
"""
from collections.abc import MutableMapping
import os

from nbconvert import LatexExporter
import nbconvert.preprocessors as pre
import nbformat

REPLACEMENTS = {
    r"\maketitle": "",
    r"\section{": r"\chapter{",
    r"\subsection{": r"\section{",
    r"\subsubsection{": r"\subsection{",
    r"\section{Problem": r"\subsection*{Problem",
    r"\section{Question": r"\subsection*{Question",
    r"\section{\texorpdfstring": r"\subsection*{\texorpdfstring",
    r"\section{Exercises": r"\section*{Exercises",
    r"\subsection{Exercise": r"\subsection*{Exercise",
    "£": r"\pounds{}",
    "\\prompt{In}{incolor}{ }{\\hspace{4pt}}\n": "",
    r"\prompt{In}{incolor}{ }{\boxspacing}": "",
}


def key(f):
    file_key = os.path.splitext(os.path.split(f)[-1])[0]
    if "-" in file_key:
        try:
            return int(file_key.split("-")[-1])
        except ValueError:
            pass
    return hash(file_key)


def execute_and_clear(notebook_file_name, source_dir, delete_repeated=True):
    nb = nbformat.read(notebook_file_name, nbformat.NO_CONVERT)
    replacements = []
    for cell in nb["cells"]:
        code_cell = cell.get("cell_type", None) == "code"
        markdown_cell = cell.get("cell_type", None) == "markdown"
        source = cell.get("source", "")
        if code_cell and ("# Setup" not in source or "### Explanation" in source):
            continue
        if markdown_cell and ("#### Discussion" in cell["source"]):
            continue
        if "metadata" in cell and "pycharm" in cell["metadata"]:
            del cell["metadata"]["pycharm"]
        replacements.append(cell)
    nb["cells"] = replacements
    executed = pre.execute.executenb(nb, cwd=source_dir)
    cop = pre.ClearOutputPreprocessor()
    nb, _ = cop.preprocess(executed, {})
    return nb


def strip_latex(notebook, replacements=None):
    replacements = REPLACEMENTS if replacements is None else replacements
    latex_exp = LatexExporter(config={})
    latex = latex_exp.from_notebook_node(notebook)
    latex_code = latex[0]
    start_str = r"\begin{document}"
    start = latex_code.find(start_str) + len(start_str)
    end = latex_code.find(r"\end{document}")
    to_export = latex_code[start:end].strip()
    for orig, repl in replacements.items():
        to_export = to_export.replace(orig, repl)
    return to_export
