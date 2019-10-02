#!/usr/bin/env python
# coding: utf-8

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




# ## Problem: Numeric indexing Series and DataFrame
# Repeat the previous questions on `y_s` and `x_df` using `.iloc`.   




# ## Problem: Selecting by Name in Series and DataFrames
# Using `x_name` and `y_name`:
# 
# 1. Select the (0,2) and the (2,0) element of `x_name`.
# 2. Select the 2nd row of `x_name` using `.loc`.
# 3. Select the 2nd columns of `x_name` using `.loc`.
# 4. Select the 2nd element of `y_name` using both `[]` and `loc`.
# 5. Select the 2nd and 4th rows and 1st and 3rd columns of `x_name`.






















# ## Problem: Selecting Data by Date
# Load the data in momentum.csv.

# Setup: Load the momentum data

import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)
momentum.head()


# 1. Select returns on February 16, 2016.
# 2. Select return in March 2016.
# 3. Select returns between May 1, 2016, and June 15, 2016









