#!/usr/bin/env python
# coding: utf-8

# # Using DataFrames
# 
# This lesson introduces:
# 
# * Basic mathematical operations on DataFrames
# * Common DataFrame methods (functions)
# * Computing percentage change (returns)
# 
# ## Problem: Addition and Subtraction
# 
# Add the prices of the three series together using `.sum(axis=1)`. Add the prices in `sep_04` to 
# the prices of `goog`. What happens? 

# Setup: Load prices
import pandas as pd
prices = pd.read_hdf('data/data.h5', 'prices')
sep_04 = pd.read_hdf('data/data.h5', 'sep_04')
goog = pd.read_hdf('data/data.h5', 'goog')








# ## Problem: Multiplication
# 
# Multiply the price of Google by 2. 




# ## Problem: Constructing portfolio returns
# Set up a vector or portfolio weights $w=\left(\frac{1}{3},\,\frac{1}{3}\,,\frac{1}{3}\right)$ and 
# compute the price of a portfolio with $\frac{1}{3}$ share of each.
# 
# *Note*: Division uses the slash operator (/). 




# ## Problem: Compute Returns
# 
# Compute returns using 
# 
# ```python
# returns = prices.pct_change()
# ```
# 
# which computes the percentage change.
# 
# Additionally, extract returns for each name using 
# 
# ```python
# spy_returns = returns['SPY']
# ```
# 










# ## Problem: Compute Log Returns
# 
# ```python
# import numpy as np
# 
# log_returns = np.log(prices).diff()
# ```
# 
# first difference of the natural log of the prices. Mathematically this is 
# $r_{t}=\ln\left(P_{t}\right)-\ln\left(P_{t-1}\right)=\ln\left(\frac{P_{t}}{P_{t-1}}\right)\approx\frac{P_{t}}{P_{t-1}}-1$.




# ## Problem: Mean, Standard Deviation and Correlation
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
# Finally, compute the correlation of the matrix of returns (`corr()`). 













# ## Problem: Summing all elements
# 
# Compute the sum of the columns of returns using `.sum()`. How is this related to the mean computed 
# in the previous step? 







# ## Problem: Maximum and Minimum Values
# Compute the minimum and maximum values of the columns of returns using the `min()` and `max()` commands. 







# ## Problem: Rounding Up, Down and to the Closest Integer
# 
# Rounding up is handled by ceil, rounding down is handled by floor and rounding to the closest 
# integer is handled by round. Try all of these commands on 100 times returns. For example,  
# ```python
# rounded = (100*returns).round()
# ``` 
# 
# Use `ceil` and `floor` to round up and down, respectively.










# ## Problem: Element-by-Element Multiplication
# 
# Mathematical commands in Python are element-by-element, except the `@` operator which is matrix 
# multiplication and uses the rules of linear algebra. 
# 
# Multiply the returns of Google and SPY together using the dot operator. 



