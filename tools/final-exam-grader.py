final_variables = globals().copy()
solutions_variables = globals().copy()

import logging
import os
import sys
import traceback

import nbformat
import numpy as np
import pandas as pd


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    green = "\x1b[32;21m"
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(levelname)s: %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger("final-exam-grader")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

path = os.path.abspath(__file__)
path = os.path.split(path)[0]
final_exam = os.path.join(path, "..", "course", "introduction", "final-exam.ipynb")
solutions = os.path.join(path, "..", "solutions", "introduction", "final-exam.ipynb")
# Ensure data/ is available
os.chdir(os.path.join(path, "..", "course", "introduction"))

if not os.path.exists(final_exam):
    logger.critical(
        "final-exam.ipynb was not found. You must have"
        "final-exam.ipynb in the directory immediately above this"
        "file."
    )
    sys.exit()

with open(final_exam, "r") as final:
    final_nb = nbformat.read(final, 4)
with open(solutions, "r") as solution:
    solution_nb = nbformat.read(solution, 4)

errors = {}
for cell in final_nb["cells"]:
    if cell["cell_type"] == "code":
        try:
            exec(cell["source"], final_variables)
        except Exception as exc:
            errors[cell["source"]] = traceback.format_exc()

for cell in solution_nb["cells"]:
    if cell["cell_type"] == "code":
        exec(cell["source"], solutions_variables)


def checker(question_number, submissions, solutions):
    question = f"QUESTION_{question_number}"
    if question not in submissions:
        logger.error(
            f"Question {question_number} is WRONG: " f"Variable {question} not found"
        )
        return 0
    wrong = False
    answer = submissions[question]
    solution = solutions[question]
    if isinstance(solution, np.ndarray):
        try:
            np.testing.assert_allclose(answer, solution)
            assert type(answer) is np.ndarray
        except AssertionError:
            wrong = True
    elif isinstance(solution, pd.DataFrame):
        try:
            pd.testing.assert_frame_equal(answer, solution)
        except AssertionError:
            wrong = True
    elif isinstance(solution, float):
        try:
            np.testing.assert_allclose(answer, solution)
        except AssertionError:
            wrong = True
    if wrong:
        logger.warning(f"Question {question_number} is WRONG")
        logger.info("Submitted Answer:")
        logger.info(answer)
        logger.info("Expected answer:")
        logger.info(solution)
        return 0
    logger.info(f"Question {question_number} is CORRECT")
    return 1


total = 0
nquestion = 20
for i in range(1, nquestion + 1):
    total += checker(i, final_variables, solutions_variables)
perc = int(100 * total / nquestion)

print()
print("-" * 80)
print(f"You correctly answered {total} out of {nquestion} ({perc}%)")
print("-" * 80)

if errors:
    split = "-" * 80 + "\n\n"
    end = "*" * 80 + "\n"
    for cell in errors:
        print(f"Cell:\n{cell}{split}\n")
        print(f"produced the error\n{errors[cell]}{end}")
