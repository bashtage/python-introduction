#!/usr/bin/env python
# coding: utf-8

#%%
# # Numeric Indexing of DataFrames
# 
# This lesson covers:
# 
# * Accessing specific elements in DataFrames using numeric indices
# 
# Accessing elements in a DataFrame is a common task. To begin this lesson,
# clear the workspace set up some vectors and a $5\times5$ array. These vectors
# and matrix will make it easy to determine which elements are selected by a
# command.
# 
# Begin by creating:
# 
# * A 5-by-5 DataFrame `x_df` containing `np.arange(25).reshape((5,5))`.
# * A 5-element Series `y_s` containing `np.arange(5)`.
# * A 5-by-5 DataFrame `x_named` that is `x_df` with columns "c0", "c1", ...,
#   "c4" and rows "r0", "r1", ..., "r4".
# * A 5-element Series `y_named` with index "r0", "r1", ..., "r4". 

#%%


#%%
# ## Problem: Picking an Element out of a DataFrame
# 
# Using double index notation, select the (0,2) and the (2,0) element of
# `x_named`.

#%%


#%%


#%%
# ## Problem: Select Elements from Series
# 
# Select the 2nd element of `y_named`.

#%%


#%%
# ## Problem: Selecting Rows as Series
# 
# Select the 2nd row of `x_named` using the colon (:) operator.
# 

#%%


#%%
# ## Problem: Selecting Rows as DataFrames
# 
# 1. Select the 2nd row of `x_named` using a slice so that the selection
#    remains a DataFrame.
# 2. Repeat using a list of indices to retain the DataFrame. 
# 

#%%


#%%


#%%
# ## Problem: Selecting Entire Columns as Series
# Select the 2nd column of `x_named` using the colon (:) operator. 

#%%


#%%
# ## Problem: Selecting Single Columns as DataFrames
# Select the 2nd column of `x_named`  so that the selection remains a DataFrame. 
# 

#%%


#%%


#%%
# ## Problem: Selecting Specific Columns
# Select the 2nd and 3rd columns of `x_named` using a slice.

#%%


#%%
# ## Problem: Select Specific Rows
# 
# Select the 2nd and 4th rows of `x_named` using a slice.  Repeat the 
# selection using a list of integers.

#%%


#%%


#%%
# ## Problem: Select arbitrary rows and columns
# 
# Combine the previous selections to the 2nd and 3rd columns and the 2nd and 4th rows
# of `x_named`. 
# 
# **Note**: This is the only important difference with NumPy.  Arbitrary
# row/column selection using `DataFrame.iloc` is simpler but less flexible.

#%%


#%%


#%%


#%%
# ## Problem: Mixed selection
# 
# Select the columns c1 and c2 and the 1st, 3rd and 5th row.

#%%


#%%
# ## Problem: Mixed selection 2
# 
# Select the rows r1 and r2 and the 1st, 3rd and final column.

#%%


#%%
# ## Exercises
# 
# ### Exercise: Select fixed length block
# 
# Compute the mean return of the momentum data in the first 66
# observations and the last 66 observations.

#%%
# Setup: Load the momentum data

import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)
momentum.head()


#%%


#%%


#%%


#%%
# ### Exercise: Compute values using fraction of sample
# 
# Compute the correlation of momentum portfolio 1, 5, and 10 in the first half of
# the sample and in the second half. 

#%%


#%%

