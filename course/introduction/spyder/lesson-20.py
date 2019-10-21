#!/usr/bin/env python
# coding: utf-8

#%%
# # Saving and Exporting Data
# 
# This lesson covers:
# 
# * Saving and reloading data
# 
# This first block loads the data that was used in the previous lesson.

#%%
# Setup: Load the data to use later
import pandas as pd

gs10_csv = pd.read_csv("data/GS10.csv", index_col="DATE", parse_dates=True)
gs10_excel = pd.read_excel("data/GS10.xls", skiprows=10,
                           index_col="observation_date")


#%%
# ## Problem: Export to Excel
# 
# Export `gs10_csv` to the Excel file `gs10-exported.xlsx`.
# 

#%%


#%%
# ## Problem: Export to CSV
# 
# Export `gs10_excel` to CSV. 

#%%


#%%
# ## Problem: Export to HDF
# 
# Export both to a single HDF file (the closest thing to a "native" format in pandas).

#%%


#%%
# ## Problem: Import from HDF 
# 
# Import the data saved as HDF and verify it is the same as the original data.

#%%


#%%


#%%
# ## Exercises
# 
# ### Exercise: Import, export and verify
# 
# * Import the data in "data/fred-md.csv"
# * Parse the dates and set the index column to "sasdate"
# * Remove first row labeled "Transform:" (**Hint**: Transpose, `del` and
#   transpose back, or use `drop`)
# * Re-parse the dates on the index
# * Remove columns that have more than 10% missing values
# * Save to "data/fred-md.h5" as HDF.
# * Load the data into the variable `reloaded` and verify it is identical.

#%%


#%%
# ### Exercise: Looping Export
# 
# Export the columns RPI, INDPRO, and HWI from the FRED-MD data to
# `"data/`_variablename_`.csv"` so that, e.g., RPI is exported to `data/RPI.csv`:
# 
# **Note** You need to complete the previous exercise first (or at least the first 4 steps).

#%%

