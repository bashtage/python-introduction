#!/usr/bin/env python
# coding: utf-8

#%%
# # Constructing DataFrames from Series
# 
# This lesson introduced method to construct a DataFrame from multiple
# Series.
# 
# This first block loads the variables created in an earlier lesson.  A
# later lesson will cover loading and saving data.

#%%
# Setup: Load data created in an earlier lesson

import pandas as pd

hdf_file = "data/dataframes.h5"

sep_04 = pd.read_hdf(hdf_file, "sep_04")
sep_05 = pd.read_hdf(hdf_file, "sep_05")
sep_06 = pd.read_hdf(hdf_file, "sep_06")
sep_07 = pd.read_hdf(hdf_file, "sep_07")
sep_10 = pd.read_hdf(hdf_file, "sep_10")
sep_11 = pd.read_hdf(hdf_file, "sep_11")
sep_12 = pd.read_hdf(hdf_file, "sep_12")
sep_13 = pd.read_hdf(hdf_file, "sep_13")
sep_14 = pd.read_hdf(hdf_file, "sep_14")
sep_17 = pd.read_hdf(hdf_file, "sep_17")
sep_18 = pd.read_hdf(hdf_file, "sep_18")
sep_19 = pd.read_hdf(hdf_file, "sep_19")

spy = pd.read_hdf(hdf_file, "spy")
aapl = pd.read_hdf(hdf_file, "aapl")
goog = pd.read_hdf(hdf_file, "goog")

dates = pd.to_datetime(pd.read_hdf(hdf_file, "dates"))

prices = pd.read_hdf(hdf_file, "prices")


#%%
# ## Problem: Construct a DataFrame from rows
# 
# Create a DataFrame named `prices_row` from the row vectors previously
# entered such that the results are identical to prices. For example, the first
# two days worth of data are:
# 
# ```python
# dates_2 = pd.to_datetime(["1998-09-04", "1998-09-05"])
# prices_row = pd.DataFrame([sep_04, sep_05])
# # Set the index after using concat to join
# prices_row.index = dates_2
# ```
# 
# Verify that the DataFrame identical by printing the difference with
# `prices` 
# 
# ```python
# print(prices_row - prices)
# ```

#%%


#%%
# ## Problem: Construct a DataFrame from columns
# 
# Create a DataFrame named `prices_col` from the 3 column vectors entered
# such that the results are identical to prices.
# 
# *Note*: `.T` transposes a 2-d array since `DataFrame` builds the
# array by rows.
# 
# Verify that the DataFrame identical by printing the difference with
# `prices` 

#%%


#%%
# ## Problem: Construct a DataFrame from a dictionary
# 
# Create a DataFrame named `prices_dict` from the 3 column vectors entered
# such that the results are identical to prices
# 
# Verify that the DataFrame identical by printing the difference with
# `prices` 

#%%

