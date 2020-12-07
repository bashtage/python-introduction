#!/usr/bin/env python
# coding: utf-8

#%%
# # Importing Data
# 
# This lesson covers:
# 
# * Importing data 
# * Converting dates 

#%%
# ## Problem: Reading in data with Dates
# 
# Read in the files `GS10.csv` and `GS10.xls` which have both been downloaded
# from [FRED](https://fred.stlouisfed.org/).

#%%


#%%
# ## Problem: Converting Dates
# 
# 1. Load the CSV file without converting the dates in `read_csv`.
# 2. Convert the date column, remove it from the DataFrame, and set it as the
#    index. 

#%%


#%%
# ## Exercises
# 
# ### Exercise: Selectively Load Columns
# 
# 1. Load the data in `data/fred-md.csv` in the columns sasdate,
#    RPI and INDPRO using the `usecols` keyword.
# 2. Remove the first row by selecting the second to the end.
# 3. Convert sasdate to dates
# 4. Set sasdate as the index and remove it from the `DataFrame`.

#%%


#%%
# ### Exercise: Load and Merge multiple Sheets
# 
# 1. Load the data on the sheet "Long Mat" in the Excel file "data/exercise.xlsx". 
#    These are 10 and 20 year constant maturity yields.
# 2. Load the data on the sheet "Short Mat" in the Excel file "data/exercise.xlsx".
#    These are 1 and 3 year constant maturity yields.
# 3. Combine the columns in the two `DataFrame`s by creating a dictionary of the keys in
#    each with the values equal to the column names.

#%%

