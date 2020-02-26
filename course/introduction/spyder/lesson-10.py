#!/usr/bin/env python
# coding: utf-8

#%%
# # Accessing Elements in DataFrames
# 
# This lesson covers:
# 
# * Assessing specific elements in Pandas Series and DataFrames 
# 
# Accessing elements in an array or a DataFrame is a common task. To begin this
# lesson, clear the workspace set up some vectors and a $5\times5$ array. These
# vectors and matrix will make it easy to determine which elements are selected
# by a command.
# 
# Start by creating 2 DataFrame and 2 Series. Define `x=np.arange(24).reshape(5,5)` 
# which is a 5 by 5 array and `y=np.arange(5)` which is a 5-element 1-d array.
# We need:
# 
# * `x_df`: A default `DataFrame` containing `x`
# * `x_named`: A `DataFrame` containing `x` with index `"r0"`, `"r1"`, ..., `"r4"` and
#   columns `"c0"`, `"c1"`, ... `"c4"`.
# * `y_s`: A default `Series` containing `y`
# * `y_named`: A `Series` containing `y` that has the index `"r0"`, `"r1"`, ..., `"r4"`

#%%


#%%
# ## Problem: Selecting a row by name
# 
# Select the 2nd row of `x_name` using `.loc`.
# 

#%%


#%%
# ## Problem: Selecting a column by name
# 
# Select the 2nd columns of `x_name` using  both `[]` and `.loc`.

#%%


#%%


#%%


#%%
# ## Problem: Selecting a elements of a Series by name
# 
# Select the 2nd element of `y_name` using both `[]` and `loc`.
# 

#%%


#%%


#%%


#%%
# ## Problem: Selecting rows and columns by name
# 
# Select the 2nd and 4th rows and 1st and 3rd columns of `x_name`.

#%%


#%%


#%%


#%%
# ## Problem: DataFrame selection with default index and column names
# 
# Select the 2nd and 4th rows and 1st and 3rd columns of `x_df`.
# 

#%%


#%%
# ## Problem: Series selection with the default index
# 
# Select the final element in `y_s`

#%%


#%%


#%%
# ## Problem: Subseries selection
# Select the subseries of `y_named` and `y_s` containing the first, fourth and fifth element.

#%%


#%%


#%%
# Load the data in momentum.csv.

#%%
# Setup: Load the momentum data

import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)
momentum.head()


#%%
# ## Problem: Selecting data on a single day
# 
# Select returns on February 16, 2016.
# 

#%%


#%%
# ## Problem: Selecting data in a single month
# 
# Select return in March 2016.

#%%


#%%
# ## Problem: Selecting data in a single year
# 
# Select return in 2016.
# 

#%%


#%%
# ## Problem: Selecting data in a date range
# 
# Select returns between May 1, 2016, and June 15, 2016.

#%%


#%%
# ## Exercises
# 
# ### Exercise: Subset time-series
# 
# Select the data for May 2017 for momentum portfolios 1 and 10.

#%%


#%%
# ### Exercise: Select using Months
# 
# Using a slice of YYYY-MM, select the returns for momentum portfolio
# 5 in the final 6 months of 2016 as `Series`

#%%


#%%
# ### Exercise: Ensure DataFrame
# 
# Repeat the previous problem but ensure the selection is a DataFrame.

#%%

