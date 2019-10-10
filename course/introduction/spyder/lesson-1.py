#!/usr/bin/env python
# coding: utf-8

#%%
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

#%%
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

#%%
# ## Running IPython in a Terminal
# 
# 1. Open a terminal.
# 2. Run IPython by entering `ipython` in the terminal window. You should see a 
#    window like the one below with the iconic `In [1]` indicating that you
#    are at the start of a new IPython session.
# 
# ![IPython in Windows Terminal](images/ipython-windows.png "IPython in Windows Terminal")

#%%
# ## Launching Jupyter notebook
# 
# 1. Launch Jupyter Notebook from the Start Menu or launcher.
# 2. Change directory to the location where you store your notebooks.
# 
# ![Jupyter Notebook](images/jupyter-notebook.png "Jupyter Notebook")

#%%
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

#%%
# ## Jupyter Notebooks in VSCode
# 
# [Visual Studio Code](https://code.visualstudio.com/) (or VS Code) is a
# lightweight IDE that supports adding features through extensions.  The
# key extension for working with notebooks is 
# [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
# The most recent version of VS Code integrates native support for Jupyter Notebooks. To create
# a Jupyter notebook:
# 
# 1. Open VS Code
# 2. Open the directory where your notebooks are stored
# 3. Open View, then Command Palette and enter the two word create jupyter. Select
#    the only option. Finally save the notebook using File, Save. **NOTE** The
#    current version may be buggy.  If you cannot use File, Save, then you can close 
#    the notebook and save it as part of closing it. 
# 
# ![VS Code New Notebook](images/vscode-new-notebook.png "VS Code New Notebook")
# 
# VS Code's notebook mode stores the notebook in a Jupyter notebook file (`.ipynb`),
# which means that you can trivially open it in any other Jupyter notebook aware app. 
# This differs from [VS code's Magic Python](#jupyter-notebooks-in-vsCode) which stores the
# file as a plain Python file (`.py`). 
# 

#%%
# ## Magic Python in VSCode
# 
# With the Python extension installed, it is possible to use a special file
# format called Magic Python to write notebook-like files that can be
# exported to Jupyter notebook files.  
# 
# 1. Install VS Code and the Python extension
# 2. Select File, New File and save with the extension .py (e.g., example.py).
# 3. This is a Python file that supports a cell demarcation using `#%%` for
#    code cells and `#%% [markdown]` for cells that contain markdown code.
#    Note that markdown text **must** be either:
#    
#    * Surrounded by triple quotes, e.g. `"""markdown text"""` or `"""markdown text"""`; e.g., 
#     ```python
#     """
#     # Cell Heading
#     
#     Likeness darkness. That give brought creeping. Doesn"t may. Fruit kind 
#     midst seed. Creature, let under created void god to. Them day was Was
#     creature set it from. Fourth. Created don"t man. Man. Light fourth
#     light given the he image first multiply after deep she"d great. Morning 
#     likeness very have give also fowl third land beast from moving thing
#     creepeth herb creeping won"t fifth. Us bring was our beast wherein our
#     void and green he fruit kind upon a given, saying fruit, moveth face 
#     forth. His you it. Good beginning hath.
#     """
#     ```
# 
#    * Or commented `# ` (with a single space) at the start of each line,
#     ```python
#     # # Cell Heading
#     #
#     # Likeness darkness. That give brought creeping. Doesn"t may. Fruit kind 
#     # midst seed. Creature, let under created void god to. Them day was Was
#     # creature set it from. Fourth. Created don"t man. Man. Light fourth
#     # light given the he image first multiply after deep she"d great. Morning 
#     # likeness very have give also fowl third land beast from moving thing
#     # creepeth herb creeping won"t fifth. Us bring was our beast wherein our
#     # void and green he fruit kind upon a given, saying fruit, moveth face 
#     # forth. His you it. Good beginning hath.
#     ```
# 
# The cells have a special button above them that allows the contents to be
# executed and the result to be displayed in the interactive window. See the 
# screenshot below for an example of the experience of using VS Code. There 
# is also an interactive console at the bottom left where commands can be 
# directly executed.
# 
# ![VS Code Notebook](images/vscode-notebook.png "VS Code Notebook")
# 

#%%
# ### Importing an exiting notebook in VS Code
# 
# VS Code only understands Magic Python files as notebook-like documents, and so
# `.ipynb` files must be converted to use. The process of importing is simple:
# 
# 1. Open a Jupyter notebook file
# 2. Click on Import in the popup that appears.
# 
# ![VS Code Export](images/vscode-export.png "VS Code Export")

#%%
# ### Exporting to an Jupyter notebook
# 
# To export a Magic Python file, open the command palette and enter "import jupyter". 
# Select the option to import the notebook.
# 
# ![VS Code Import](images/vscode-import.png "VS Code Import")

#%%
# ## Jupyter notebooks in PyCharm Professional
# 
# <div class="alert alert-info">
# PyCharm Professional is my recommended approach if you are going to use Python
# throughout the course. It provides the best experience and can be acquired for
# free using the student program.
# </div>
# 
# PyCharm Professional has deeply integrated Jupyter Notebooks. To create
# an Jupyter notebook:
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
# 
# ### Magic Python in PyCharm
# PyCharm supports Magic Python cell execution. To use Magic Python, you need
# to enable *Scientific Mode* in the View menu. You can then use `#%%` to
# indicate the start and end of cells. Individual Cells can be executed in
# the console by pressing CTRL+Enter.
# 
# 1. In PyCharm, right-click on the root directory and select `New > Python File`. Give
#    your file a meaningful name.
# 2. Enter
#    ```python
#    #%%
#    print("This is the first cell")
#    
#    #%%
#    print("This is not executed when the first cell is run") 
#    ```
# 3. Enable Scientific Mode in the View menu.
# 4. Run the first cell by placing you mouse in the cell and pressing CTRL+Enter.
# 5. Run the second cell by clicking on the Play button (arrow) that appears in the
#    gutter of the editor.
# 
# <div class="alert alert-warning">
# <b>Note:</b> Magic Python in PyCharm only supports python code, and so it is
# not possible to mix Markdown text and Python in the same file.
# </div>
#    
