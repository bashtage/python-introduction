#!/usr/bin/env python
# coding: utf-8

# # Calling Functions
# 
# This lesson covers:
# 
# * Calling functions with more than one input and output 
# * Calling functions when some inputs are not used

# Read the data in momentum.csv and creating some variable. This cell uses some magic to automate 
# repeated typing.

# Setup: Load the momentum data
import pandas as pd

momentum = pd.read_csv('data/momentum.csv')

print(momentum.head())

mom_01 = momentum['mom_01']
mom_10 = momentum['mom_10']


# This data set contains 2 years of data on the 10 momentum portfolios from 2016–2018. The variables
# are named mom_XX where XX ranges from 01 (work return over the past 12 months) to 10 (best return 
# over the past 12 months). 

# ## Problem: Calling Functions
# Functions were used in the previous lesson. Get used to calling functions by computing the mean,
# std, kurtosis, max, and min of the 10 momentum portfolios. Also, explore the help 
# available for calling functions `?` operator. For example,
# 
# ```python
# momentum.std?
# ```  
# 
# opens a help window that shows the inputs and output, while
# 
# ```python
# help(momentum.std)
# ```
# 
# shows the help.
# 
# Use the functions `mean`, `std`, `skew` and `kurt` to print the
# values for `mom_01`.




# ## Problem: Use NumPy and SciPy functions
# 
# Use the NumPy functions `mean` and `std` and the SciPy `stats` functions
# `skew` and `kurtosis` to produce the same output.




# ## Problem: Calling Functions with 2 Outputs
# 
# Some useful functions return 2 or more outputs. One example is ``np.linalg.slogdet`` 
# computes the signed log determinant of a square array. It returns two output,
# the sign and the log of the absolute determinant.
# 
# Use this function to compute the sign and log determinant of the 2 by 2 array:
# 
# ```
# 1  2
# 2  9
# ```  




# ## Problem: Calling Functions with 2 Inputs
# 
# Many functions take two or more inputs. Like outputs, the inputs are simply listed in order
# separated by commas. Use `np.linspace` to produce a series of 11 points evenly spaced between 0 
# and 1.  




# ## Problem: Calling Functions using Keyword Arguments
# 
# Many functions have optional arguments. You can see these in a docstring since
# optional arguments take the form `variable=default`. For example, see
# the help for `np.mean`




# which is 
# 
# ```python
# pd.DataFrame.std(self, axis=None, skipna=None, level=None, ddof=1, numeric_only=None)
# ```
# 
# `std`  computes the standard deviation.
# 
# This tells us that only `self` (which is the DataFrame) is required and that the other 5 inputs
# can be omitted if you are happy with the defaults.  However, if we want to change some
# of the optional inputs, then we can directly use the inputs name in the function call.
# 
# By default `std` divides by `n-1`.  The `1` can be set using `ddof`.
# 
# Compute `std` using `ddof=0` on the momentum data.






