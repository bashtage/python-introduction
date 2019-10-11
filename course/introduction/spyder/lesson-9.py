#!/usr/bin/env python
# coding: utf-8

#%%
# # Common DataFrame methods
# 
# This lesson introduces the common `DataFrame` methods that
# we will repeatedly use in the course. 
# 
# This first cell load data for use in this lesson.

#%%
# Setup: Load prices
import pandas as pd
prices = pd.read_hdf("data/dataframes.h5", "prices")
sep_04 = pd.read_hdf("data/dataframes.h5", "sep_04")
goog = pd.read_hdf("data/dataframes.h5", "goog")
returns = prices.pct_change().dropna()
spy_returns = returns.SPY
aapl_returns = returns.AAPL
goog_returns = returns.GOOG


#%%
# ## Problem: Constructing portfolio returns
# 
# Compute the return of a portfolio with weight $\frac{1}{3}$ in each security using
# multiplication (`*`) and `.sum()`.
# 
# **Note**: You need to use the `axis` keyword for the sum.

#%%


#%%
# ## Problem: Compute the Mean and Standard Deviation
# 
# Using the function mean, compute the mean of the three returns series one at a time. For example  
# ```python
# goog_mean = goog_returns.mean()
# ```
# Next, compute the mean of the matrix of returns using  
# 
# ```python
# retmean = returns.mean()
# ```
# 
# What is the relationship between these two? Repeat this exercise for the standard deviation (`std()`).
# 

#%%


#%%


#%%


#%%
# ## Problem: Compute Correlation
# Compute the correlation of the matrix of returns (`corr()`). 

#%%


#%%
# ## Problem: Summing all elements
# 
# Compute the sum of the columns of returns using `.sum()`. How is this related to the mean computed 
# in the previous step? 

#%%


#%%


#%%
# ## Problem: Maximum and Minimum Values
# Compute the minimum and maximum values of the columns of returns using the `min()` and `max()` commands. 

#%%


#%%


#%%
# ## Problem: Rounding Up, Down and to the Closest Integer
# 
# Rounding up is handled by ceil, rounding down is handled by floor and rounding to the closest 
# integer is handled by round. Try all of these commands on 100 times returns. For example,  
# ```python
# rounded = (100*returns).round()
# ``` 
# 
# Use `ceil` and `floor` to round up and down, respectively.

#%%


#%%


#%%

