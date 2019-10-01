#!/usr/bin/env python
# coding: utf-8

# # Series and DataFrames
# 
# This lesson covers:
# 
# * Manually inputting data in scalars, vectors, and matrices 
# * Basic mathematical operations 
# * Saving and loading data 
# 
# <a id="stock-data"></a>
# ## Data
# September 2018 prices (adjusted closing prices) for the S&P 500 EFT (SPY), Apple (AAPL) and 
# Google (GOOG) are listed below:
# 
# 
# 
# | Date   | SPY Price | AAPL Price | GOOG Price | 
# |:-------|----------:|-----------:|-----------:| 
# | Sept4  | 289.81    | 228.36     | 1197.00    | 
# | Sept5  | 289.03    | 226.87     | 1186.48    | 
# | Sept6  | 288.16    | 223.10     | 1171.44    | 
# | Sept7  | 287.60    | 221.30     | 1164.83    | 
# | Sept10 | 288.10    | 218.33     | 1164.64    | 
# | Sept11 | 289.05    | 223.85     | 1177.36    | 
# | Sept12 | 289.12    | 221.07     | 1162.82    | 
# | Sept13 | 290.83    | 226.41     | 1175.33    | 
# | Sept14 | 290.88    | 223.84     | 1172.53    | 
# | Sept17 | 289.34    | 217.88     | 1156.05    | 
# | Sept18 | 290.91    | 218.24     | 1161.22    | 
# | Sept19 | 291.44    | 216.64     | 1158.78    | 
# 
# **Prices in September 2018**
#  

# ## Problem: Input scalar data
# 
# Create 3 variables, one labeled `spy`, one labeled `aapl` and one labeled `goog` that contain the
# September 4 price of the asset. For example, to enter the Google data
# ```python
# goog = 1197.00
# ```




# ## Problem: Print the values
# Print the values of the three variables you created in the previous step using `print`.




# ## Problem: Print the values with formatting
# Print the values of the three variables you created in the previous step using format strings following
# the pattern TICKER: Value. For example, you can print the value of Google using `print(f'GOOG: {goog}')`.




# ## Problem: Input a Vector
# 
# Create vectors for each of the days in the [Table](#stock-data) named `sep_xx` where `xx` is the 
# numeric date. For example,  
# ```python
# import pandas as pd
# 
# sep_04 = pd.Series([289.81,228.36,1197.00], index=['SPY','AAPL','GOOG']);
# ```




# ## Problem: Create a Vector of Dates
# 
# Use the pandas function `pd.to_datetime` to convert a list of string dates to a pandas 
# `DateTimeIndex`, which can be used to set dates in other arrays. For example, the first two dates 
# are
# ```python
# dates_2 = pd.to_datetime(['4-9-2018','5-9-2018'])
# print(dates_2)
# ```
# which produces
# ```python
# DatetimeIndex(['2018-04-09', '2018-05-09'], dtype='datetime64[ns]', freq=None)
# ```
# 
# Create a vector containing all of the dates in the table.




# ## Problem: Input a Vector with Dates
# 
# Create vectors for each of the ticker symbols in [Table](#stock-data) named spy, aapl and 
# goog, respectively. Use the variable `dates` that you created in the previous step. 
# 
# For example
# 
# ```python
# goog = pd.Series([1197.00,1186.48,1171.44,...], index=dates)
# ```




# ## Problem: Create a DataFrame
# 
# Create a DataFrame named `prices` containing [Table](#stock-data). Set the column names equal to 
# the ticker and set the index to the dates you created previously.
# 
# ```python
# prices = pd.DataFrame([[289.81, 228.36, 1197.00], [289.03, 226.87, 1186.48]],
#                       columns = ['SPY', 'AAPL', 'GOOG'],index=dates_2)
# ```




# ## Problem: Construct a DataFrame from Series
# 
# Create a second DataFrame named prices_row from the row vectors previously entered such that 
# the results are identical to prices. For example, the first two days worth of data are
# 
# ```python
# pricess_row = pd.DataFrame([Sep04, Sep05])
# # Set the index after using concat to join
# pricess_row.index = dates_2
# ```
# 
# Create a third DataFrame named prices_col from the 3 column vectors entered such that the results 
# are identical to prices
# ```python
# prices_col = pd.DataFrame([SPY,APPL,GOOG]).T
# ```
# 
# *Note*: The `.T` above transposes the 2-d array since `DataFrame` builds the array by rows.
# 
# Verify that all three matrices are identical by printing the difference, e.g., 
# 
# ```python
# print(pricescol - prices)
# ```
# 
# and that all elements are 0. 




# Save the price data
# 
# This block saves prices to a HDF file for use in later lessons. The
# function used to save the data is covered in a later lesson.

# Setup: Save prices, goog and sep_04 into a single file for use in other lessons

# Only run if prices has been defined
if 'prices' in globals():
    with pd.HDFStore('data/data.h5', mode='w') as h5:
        h5.put('prices', prices)
        h5.put('goog', goog)
        h5.put('sep_04', sep_04)

