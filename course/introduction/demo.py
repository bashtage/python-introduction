# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Demonstration
# 
# This file is used to demonstrate interacting with Jupyter notebooks
# in
# 
# * VS Code
# * PyCharm Professional
# * Jupyter notebook server
# 
# This code is used to illustrate the behavior of each of the platforms
# and. It is not necessary to understand the code itself at the beginning
# of the course.  The introduction will provide explanation of code used
# here. 

# %%
import numpy as np

x = 2 * np.pi
print(f"The value of 2π is {2 * np.pi}")  


# %%
import pandas as pd
df = pd.read_csv("data/momentum.csv", parse_dates=True, index_col="date")
df.head()


# %%
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import seaborn
plt.rc("figure", figsize=(16,6))
seaborn.set_style("darkgrid")

e = np.random.standard_normal(100)
y = np.cumsum(e)
ax = plt.plot(y)

# %% [markdown]
# # Title
# ## Chapter
# ### Section
# 
# This is an example of a markdown cell.  You can use **bold**, _italics_, and
# `monospace` formatting.  You can also have code blocks.
# 
# ```python
# for i in range(10):
#     print(i)
# ```
# 
# Markdown cells also support both inline math, $\alpha+\beta=\gamma$ or entire
# lines,
# 
# $$ f(x) = \frac{1}{2\pi}\exp\left(-\frac{x^2}{2}\right),$$
# 
# using $\LaTeX$ code. 
# 
# You can also include tables,
# 
# | Parameter | Value |
# |-----------|-------|
# | $\alpha$  | 0.05  |
# | $\beta$   | 0.90  |

# %%



