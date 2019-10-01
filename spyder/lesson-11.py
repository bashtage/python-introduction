#!/usr/bin/env python
# coding: utf-8

# # Program Flow
# 
# This lesson covers:
# 
# * for loops 
# * Nested loops 
# 
# 

# ## Problem: Basic For Loops
# 
# Construct a for loop to sum the numbers between 1 and N for any N. A for loop that does nothing can be written:
# 
# ```python
# n = 10
# for i in range(n):
#     pass
# ```
# 




# ## Problem: Compute a compound return
# The compound return on a bond that pays interest annually at rate r is given by 
# $cr_{t}=\prod_{i=1}^{T}(1+r)=(1+r)^{T}$. Use a for loop compute the total return for 
# £100 invested today for $1,2,\ldots,10$ years. Store this variable in a 10 by 1 vector cr. 
# 




# ## Problem: Simulate a random walk
# (Pseudo) Normal random variables can be simulated using the command
# `np.random.standard_normal(shape)` where `shape` is a tuple (or a scalar) containing the 
# dimensions of the desired random numbers. Simulate 100 normals in a 100 by 1 vector and name 
# the result `e`. Initialize a vector `p` containing zeros using the function zeros. Add the 
# 1st element of `e` to the first element of `p`. Use a for loop to simulate a process 
# $y_{i}=y_{i-1}+e_{i}$. When finished plot the results using
# 
# ```python
# %matplotlib inline
# 
# import matplotlib.pyplot as plt
# plt.plot(y)
# ```
# 







# ## Problem: Nested Loops
# Begin by loading momentum data used in an earlier lesson. Begin by adding 1 to the returns to
# produce gross returns. The gross return is the total value in the current period of £1 invested 
# in the previous period. A net return subtracts the original investment to produce the net gain 
# or loss. Use two loops to loop both across time and across the 10 portfolios to compute the 
# total compound return. 
# 
# For example, if only interested in a single series,
# 
# ```python
# n = mom_01.shape[0]
# cr=np.zeros(n) 
# gr = 1 + mom_01 
# cr[0] = 1+mom_01[0] 
# for t in range(1, n):
#     cr[t]=cr[t-1]*gr[t] 
# ```
# computes the cumulative return.
# 
# When finished, plot the cumulative returns using `plt.plot(cr)`. After finishing this problem,
# have a look at `np.cumsum?` and `np.cumprod?`. 

# Setup: Load the momentum data

import pandas as pd
momentum = pd.read_csv('data/momentum.csv', index_col='date', parse_dates=True)
momentum = momentum / 100  # Convert to numeric values from percentages
# Convert to a plain numpy array
momentum = momentum.to_numpy()








# ## Exercises
# 
# ### Exercise
# 1. Simulate a 1000 by 10 matrix consisting of 10 standard random walks using both nested loops
#    and `np.cumsum`. 
# 2. Plot the results. 
# 
# **Question to think about**
# 
# If you rerun the code in this Exercise, do the results change? Why? 
