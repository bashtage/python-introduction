#!/usr/bin/env python
# coding: utf-8

# %%
# # Getting Started
#
# This lesson covers:
#
# * Opening a terminal window
# * Launching Jupyter notebook
# * Running IPython in a Terminal
# * Running IPython in Jupyter QtConsole
# * Executing a standalone Python file in IPython
# * Optional
#   * Jupyter notebooks in [VSCode](https://code.visualstudio.com/docs/python/jupyter-support)
#   * Jupyter notebooks in [PyCharm Professional](https://jetbrains.com/student/)

# %%
# ## Opening an Anaconda Terminal
#
# An Anaconda terminal allows `python` to be run directly.  It also allows other
# useful programs, for example `pip`, the Python package manager to be used to
# install packages that are not available through Anaconda.
#
# ### Windows
#
# Launch Anaconda Prompt from the start menu.
#
# ### OSX and Linux
# Open the terminal (instructions depend on your distribution). If you allowed
# conda to initialize, then you should be ready to call Anaconda"s python and
# supporting functions.  If not, you should
#
# ```
# cd ~/anaconda3/bin
# ./conda init
# ```
#
# and then reopen your terminal.
#

# %%
# ## Running IPython in a Terminal
#
# 1. Open a terminal.
# 2. Run IPython by entering `ipython` in the terminal window. You should see a
#    window like the one below with the iconic `In [1]` indicating that you
#    are at the start of a new IPython session.
#
# ![IPython in Windows Terminal](images/ipython-windows.png "IPython in Windows Terminal")

# %%
# ## Launching Jupyter Lab
#
# 1. Launch Jupyter Lab from the Start Menu or launcher.
# 2. Change directory to the location where you store your notebooks.
#
# ![Jupyter Notebook](images/jupyter-lab.png "Jupyter Lab")

# %%
# ## Executing a standalone Python file in IPython
#
# 1. Open a text editor and enter the following lines. Save the file as
#    lesson-2.py. Note that Python is white-space sensitive, and so these
#    lines should **not** not indented.
#
# ```python
# from math import exp, log
#
# x = exp(1)
# y = log(x)
#
# print(f"exp(1)={x}, log(exp(1))={y}")
# ```
#
# 2. Run the code in an IPython session using `%run -i lesson-2.py`.  Note: you
#    should create the python file in the same directory as the notebook.
#
# If everything works as expected, you should see
#
# ```python
# exp(1)=2.718281828459045, log(exp(1))=1.0
# ```

# %%
# ## Jupyter notebooks in VSCode
#
# [Visual Studio Code](https://code.visualstudio.com/) (or VS Code) is a
# lightweight IDE that supports adding features through extensions.  The
# key extension for working with notebooks is
# [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
# With this extension installed, VS code provides native support for
# Jupyter notebooks.
#
# 1. Install VS Code and the Python extension
# 2. Use File>New File...>Jupyter Notebook to create a new notebook.
#
# See the screenshot below for an example of the experience of using Jupyter notebooks in
# VS Code.
#
# ![VS Code Notebook](images/vscode-notebook-new.png "VS Code Notebook")
#

# %%
# ## Jupyter notebooks in PyCharm Professional
#
# <div class="alert alert-info">
# PyCharm Professional is my recommended approach if you are going to use Python
# throughout the course. It provides the best experience and can be acquired for
# free using the student program.
# </div>
#
# PyCharm Professional has deeply integrated Jupyter Notebooks. To create
# an IPython notebook:
#
# 1. Open PyCharm Profession
# 2. Open the directory where your notebooks are stored
# 3. Right-click on the root directory and select `New > Jupyter Notebook`.
#    Give your file a meaningful name, and it will open in the main window.
#
# ![PyCharm New Notebook](images/pycharm-new-notebook.png "PyCharm New Notebook")
#
# PyCharm uses a special syntax where cells look like code and so can be edited
# like text. This allows PyCharm to use introspection and code completion on the
# code you have written, a highly useful set of features. PyCharm stores the
# notebook in a Jupyter notebook file (`.ipynb`), which means that you can
# trivially open it in any other Jupyter notebook aware app.  This differs from
# [VS code](#jupyter-notebooks-in-vsCode) which stores the file as a play Python
# file (`.py`) and requires an explicit export to a Jupyter notebook file.
#
# A code cell is demarcated using `#%%` and a markdown cell begins with `#%% md`.
# Below is a screenshot of this notebook in PyCharm.
#
# ![PyCharm Notebook](images/pycharm-notebook.png "Pycharm Notebook")
