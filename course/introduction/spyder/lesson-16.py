#!/usr/bin/env python
# coding: utf-8

#%%
# # Logic and Loops
# 
# This lesson covers:
# 
# * Mixing logic and loops 
# 
# Begin by loading the data in momentum.csv.
# 

#%%
# Setup: Load the momentum data

import numpy as np
import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)

print(momentum.head())

mom_01 = momentum["mom_01"]
mom_10 = momentum["mom_10"]
mom_05 = momentum["mom_05"]


#%%
# ## Problem: Logical Statements and for Loops
# Use a for loop along with an `if` statement to simulate an asymmetric random
# walk of the form 
# 
# $$y_{i}=y_{i-1}+e_{i}+I_{[e_{i}<0]}e_{i}$$
# 
# where $I_{[e_{i}<0]}$ is known as an indicator variable that takes the value
# 1 if the statement in brackets is true. Plot y. $e$ is a standard normal
# shock. Use `cumsum` to simulate a symmetric one (`z`), and plot the two using
# the code in the cell below.
#  

#%%


#%%
# Plot the two random walks using the code.  We will cover data visualization
# in a later lesson. 
# 
# ```python
# %matplotlib inline
# import matplotlib.pyplot as plt
# plt.plot(y)
# plt.plot(z)
# plt.legend(["y", "z"])
# ```

#%%


#%%
# ## Problem: Simulate the asymmetricc random walk without an `if`-`then`
# 
# Use boolean multiplication to simulate the same random walk without using
# an `if`-`then` statement. 

#%%


#%%
# Setup: Plot the data
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')


#%%


#%%
# ## Problem: Selecting Elements using Logical Statements
# For portfolio 1 and portfolio 10, select the elements that are $<0$,
# $\geq 0$ and exactly equal to $0$. Next select the elements where both
# portfolios are less than $0$. 
# 

#%%


#%%


#%%

