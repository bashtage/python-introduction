#!/usr/bin/env python
# coding: utf-8

# %%
# ## Data Set Construction
#
# **Functions**
#
# `pd.read_csv`, `pd.read_excel`, `np.diff` or `DataFrame.diff`, `DataFrame.resample`
#
# ### Exercise 1
#
# 1. Download all available daily data for the S&P 500 and the Hang Seng Index from Yahoo! Finance.
# 2. Import both data sets into Python. The final dataset should have a `DateTimeIndex`, and the date
#    column should not be part of the `DataFrame`.
# 3. Construct weekly price series from each, using Tuesday prices (less likely to be a holiday).
# 4. Construct monthly price series from each using last day in the month.
# 5. Save the data to the HDF file "equity-indices.h5".
#

# %%


# %%
# ### Exercise 2
#
# Write a function that will correctly aggregate to weekly or monthly respecting the
# aggregation rules
#
# * High: `max`
# * Low: `min`
# * Volume: `sum`
#
# The signature should be:
#
# ```python
# def yahoo_agg(data, freq):
#     <code here>
#     return resampled_data
# ```
#

# %%


# %%
# ### Exercise 3
#
# 1. Import the Fama-French benchmark portfolios as well as the 25 sorted portfolios at both the
#    monthly and daily horizon from [Ken French"s Data Library](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).
#    **Note** It is much easier to clean to data file before importing than to find the precise
#    command that will load the unmodified data.
# 2. Import daily FX rate data for USD against AUD, Euro, JPY and GBP from the [Federal Reserve Economic Database (FRED)](http://research.stlouisfed.org/fred2/categories/94). Use Excel (xls) rather than csv files.
# 3. Save the data to the HDF files "fama-french.h5" and "fx.h5"

# %%


# %%
# ### Exercise 3 (Alternative method)
#
# 1. Install and use `pandas-datareader` to repeat the previous exercise.
#
# #### Preliminary Step
#
# You must first install the module using
#
# ```
# pip install pandas-datareader
# ```
#
# from the command line. Then you can run this code. **Note**: Running this code requires access
# to the internet.

# %%


# %%
# ### Exercise 4
# Download data on 1 year and 10 year US government bond rates from FRED, and
# construct the term premium as the different in yields on 10 year and 1 year
# bonds. Combine the two yield series and the term premium into a `DataFrame`
# and save it as HDF.

# %%
