#!/usr/bin/env python
# coding: utf-8

#%%
# # Using Boolean arrays 
# 
# This lesson covers:
# 
# * `all` and `any`
# * `where`
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
# ## Problem: Using `where`
# Use `where` to select the index of the elements in portfolio 5 that are
# negative. Next, use the `where` command in its two output form to determine
# which elements of the portfolio return matrix are less than -2%.

#%%


#%%


#%%


#%%
# ## Problem: Combining flow control
# For momentum portfolios 1 and 10, compute the length of the runs in the
# series. In pseudo code,
# 
# * Start at i=1 and define run(1) = 1
# * For i in 2,...,T, define run(i) = run(i-1) + 1 if 
#   $\textrm{sgn}\left(r_{i}\right)=\textrm{sgn}\left(r_{i-1}\right)$ else 1.
# 
# You will need to use `len` and `zeros`. 
# 
# 1. Compute the length longest run in the series and the index of the
#    location of the longest run. Was it positive or negative?
# 2. How many distinct runs lasted 5 or more days?

#%%


#%%
# Plot the runs using 
# 
# ```python
# %matplotlib inline
# 
# import matplotlib.pyplot as plt
# plt.plot(run)
# ```

#%%


#%%
# ## Problem: Use `any` to find large losses
# 
# Use any to determine if any of the 10 portfolios experienced a loss
# greater than -5%.

#%%


#%%


#%%


#%%
# Use `all` and negation to do the same check as `any`.

#%%


#%%
# ## Exercises
# 
# ### Exercise: all and any
# Use all to determine the number of days where all of the portfolio returns
# were negative. Use any to compute the number of days with at least 1 negative
# return and with no negative returns (Hint: use negation (~ or `logical_not`)). 
