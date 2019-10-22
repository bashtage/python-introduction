#!/usr/bin/env python
# coding: utf-8

#%%
# # Methods and Functions
# 
# This lesson covers:
# 
# * Calling functions with more than one input and output 
# * Calling functions when some inputs are not used

#%%
# Read the data in momentum.csv and creating some variable. This cell uses
# some magic to automate repeated typing.

#%%
# Setup: Load the momentum data
import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)

print(momentum.head())

mom_01 = momentum["mom_01"]
mom_10 = momentum["mom_10"]


#%%
# This data set contains 2 years of data on the 10 momentum portfolios from
# 2016–2018. The variables are named mom_XX where XX ranges from 01 (work
# return over the past 12 months) to 10 (best return over the past 12 months). 

#%%
# ## Problem: Calling Methods
# Get used to calling methods by computing the mean, standard deviation, skewness, kurtosis, max, and min. 
# 
# Use the DataFrame functions `mean`, `std`, `skew` and `kurt`, `min` and `max` to print the
# values for `mom_01`.
# 
# In the second cell, call `describe`, a method that summarizes `Series` and `DataFrames` on `mom_01`.

#%%


#%%


#%%
# ## Problem: Use NumPy and SciPy functions
# 
# Use the NumPy functions `mean`, `std`, `min`, `max` and the SciPy `stats` functions
# `skew` and `kurtosis` to produce the same output.

#%%


#%%
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

#%%


#%%


#%%
# ## Problem: Calling Functions with 2 Inputs
# 
# Many functions take two or more inputs. Like outputs, the inputs are simply
# listed in order separated by commas. Use `np.linspace` to produce a series
# of 11 points evenly spaced between 0 and 1.
# 
# ```
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# ```  

#%%


#%%
# ## Problem: Calling Functions using Keyword Arguments
# 
# Many functions have optional arguments. You can see these in a docstring since
# optional arguments take the form `variable=default`. For example, see
# the help for `scipy.special.comb`, which has the function signature
# 
# ```
# comb(N, k, exact=False, repetition=False)
# ```
# 
# This tells us that `N` and `k` are required and
# that the other 2 inputs can be omitted if you are happy with the defaults.
# However, if we want to change some of the optional inputs, then we can
# directly use the inputs name in the function call.
# 
# Compute the number of distinct combinations of 5 objects from a set of 10.

#%%


#%%
# Compute the total number of combinations allowing for repetition 
# using the `repetition=True` keyword argument.

#%%


#%%
# Compute the number of combinations using the exact representation using 
# only positional arguments for all 3 inputs.  Repeat using the keyword
# argument for `exact`.

#%%


#%%


#%%
# ## Problem: Function Help
# 
# Explore the help available for calling functions `?` operator. For example,
# 
# ```python
# import scipy.stats as stats
# 
# stats.kurtosis?
# ```  
# 
# opens a help window that shows the inputs and output, while
# 
# ```python
# help(stats.kurtosis)
# ```
# 
# shows the help in the console.
# 
# **Note**: VS Code does **not** support the `?` form of help

#%%


#%%


#%%
# ## Problem: Use `help` with a method
# 
# Use `help` to get the help for the `kurt` method attached to `momentum`.

#%%


#%%
# ## Exercises
# 
# ### Exercise: Use `info`
# 
# Use the `info` method on `momentum` to get information about this `DataFrame`.

#%%


#%%
# ### Exercise: Compute the day-by-day mean
# 
# Compute the day-by-day mean return of the portfolios in the momentum `DataFrame` using
# the `axis` keyword argument. Use `head` and `tail` to show
# the first 5 rows and last 5 rows 

#%%


#%%


#%%
# ### Exercise: Compute the standard deviation of mean returns
# 
# Compute the standard deviation of the mean returns by chaining methods.

#%%


#%%
# ### Exercise: Compute the average standard deviation
# 
# Compute the mean standard deviation as:
# 
# $$ \sqrt{N^{-1} \sum_{i=1}^N V[r_i]} $$
# 
# where $V[r_i]$ is the variance of portfolio $i$.

#%%

