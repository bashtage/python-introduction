#!/usr/bin/env python
# coding: utf-8

#%%
# # Boolean Selection 
# 
# This lesson covers:
# 
# * Boolean selection
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


#%%
# ## Problem: Selecting rows with boolean conditions
# 
# Select the rows in `momentum` where all returns on a day are negative.

#%%


#%%
# ## Problem: Selecting rows
# 
# Select the rows in `momentum` where 50% or more of the returns on a day are negative.

#%%


#%%
# ## Problem: Selecting columns
# 
# Select the columns in `momentum` what have the smallest and second smallest average returns.

#%%


#%%


#%%


#%%
# ## Problem: Selecting rows and columns
# 
# Select the returns for the column with the single most negative return
# on days where all of the returns are negative. 

#%%


#%%


#%%
# ## Problem: Selecting Elements using Logical Statements
# For portfolio 1 and portfolio 10 compute the correlation when both 
# returns are negative and when both are positive.
# 

#%%


#%%


#%%
# Setup: Reproducible random numbers

rs = np.random.RandomState(19991231)
x = rs.randint(1, 11, size=(10,3))
x


#%%
# ## Problem: Select the columns of x that means >= $E[x]$

#%%


#%%
# ## Problem: Select the rows of x that means >= $E[x]$

#%%


#%%
# ## Problem: Select the rows and column of x where both have means < $E[x]$

#%%


#%%
# ## Problem: Using `where`
# Use `where` to select the index of the elements in portfolio 5 that are
# negative. Next, use the `where` command in its two output form to determine
# which elements of the portfolio return matrix are less than -2%.

#%%


#%%


#%%


#%%
# ## Exercises
# 
# ### Exercise: Select the Most Volatile Portfolio
# 
# Select the column in momentum that has the highest standard deviation.

#%%


#%%
# ### Exercise: Select the High Kurtosis Portfolios
# 
# Select the columns that have kurtoses above the median kurtosis.

#%%


#%%
# ### Exercise: Select 
# 
# Select the rows where all of the returns in the row are less than the 25%
# quantile for their portfolio.
# 
# **Note**: Comparisons between `DataFrame`s and `Series` works like mathematical
# operations (`+`, `-`, etc.).

#%%


#%%

