"""
Prepare notebooks for PDF export via LaTeX
"""
from collections.abc import MutableMapping
import distutils.dir_util
import glob
import os
import shutil
import subprocess

from nbconvert import LatexExporter
import nbconvert.preprocessors as pre
import nbformat

base_dir = os.path.abspath("..")
latex_dir = os.path.join("..", "tex")
source_dir = "../solutions/"
nb_files = glob.glob(os.path.join(source_dir, "*.ipynb"))

for nb_file in nb_files:
    print(f"Processing {nb_file}")
    nb = nbformat.read(nb_file, nbformat.NO_CONVERT)
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

    _, base = os.path.split(nb_file)
    out = os.path.abspath(os.path.join("..", base))
    latex_exp = LatexExporter(config={})
    latex = latex_exp.from_notebook_node(nb)
    base, _ = os.path.splitext(base)
    latex_code = latex[0]
    start_str = r"\begin{document}"
    start = latex_code.find(start_str) + len(start_str)
    end = latex_code.find(r"\end{document}")
    to_export = latex_code[start:end].strip()
    replacements = {
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
    for orig, repl in replacements.items():
        to_export = to_export.replace(orig, repl)
    if base == "lesson-1":
        to_export = to_export.replace("\section{", "\section*{")
    with open(os.path.join(latex_dir, base + ".tex"), "w") as output:
        output.write(to_export)

distutils.dir_util.copy_tree(
    os.path.join(source_dir, "images"), os.path.join(latex_dir, "images")
)
cwd = os.path.abspath(latex_dir)
os.chdir(cwd)
tex_file = os.path.join(cwd, "python-introduction.tex")
subprocess.run(["pdflatex", tex_file], cwd=cwd)
subprocess.run(["pdflatex", tex_file], cwd=cwd)

print("Copying file to final location.")
pdf_file = tex_file.replace(".tex", ".pdf")
pdf_file_name = os.path.split(pdf_file)[1]
target = os.path.abspath(os.path.join("..", pdf_file_name))
print(pdf_file)
print(target)
shutil.copyfile(pdf_file, target)
