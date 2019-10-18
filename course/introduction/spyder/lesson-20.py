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

