"""
Tools for manipulating the LaTeX produced from notebooks
"""
from collections.abc import MutableMapping

import nbconvert.preprocessors as pre
import nbformat
from nbconvert import LatexExporter

REPLACEMENTS = {
    r"\maketitle": "",
    r"\section{": r"\chapter{",
    r"\subsection{": r"\section{",
    r"\subsubsection{": r"\subsection{",
    r"\section{Problem": r"\subsection*{Problem",
    r"\section{\texorpdfstring": r"\subsection*{\texorpdfstring",
    r"\section{Exercises": r"\section*{Exercises",
    r"\subsection{Exercise": r"\subsection*{Exercise",
    "£": r"\pounds{}",
    "\\prompt{In}{incolor}{ }{\\hspace{4pt}}\n": "",
}


def execute_and_clear(notebook_file_name, source_dir):
    nb = nbformat.read(notebook_file_name, nbformat.NO_CONVERT)
    replacements = []
    for cell in nb["cells"]:
        if isinstance(cell, MutableMapping):
            if cell["cell_type"] == "code" and "# Setup" not in cell["source"]:
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
