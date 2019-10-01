#!/usr/bin/env python
# coding: utf-8

# # Logic and Loops
# 
# This lesson covers:
# 
# * Mixing logic and loops 
# * `all` and `any` 
# 
# Begin by loading the data in momentum.csv.
# 

# Setup: Load the momentum data

import numpy as np
import pandas as pd

momentum = pd.read_csv('data/momentum.csv', index_col='date', parse_dates=True)

print(momentum.head())

mom_01 = momentum['mom_01']
mom_10 = momentum['mom_10']
mom_05 = momentum['mom_05']


# ## Problem: Logical Statements and for Loops
# Use a for loop along with an `if` statement to simulate an asymmetric random
# walk of the form 
# 
# $$y_{i}=y_{i-1}+e_{i}+I_{[e_{i}<0]}e_{i}$$
# 
# where $I_{[e_{i}<0]}$ is known as an indicator variable that takes the value
# 1 if the statement in brackets is true. Plot y. $e$ is a standard normal
# shock. Use `cumsum` to simulate a symmetric one (`z`), and plot the two using
# the code in the cell below.
#  










# ## Problem: Simulate the asymmetricc random walk without an `if`-`then`
# 
# Use boolean multiplication to simulate the same random walk without using
# an `if`-`then` statement. 




# Setup: Plot the data
get_ipython().run_line_magic('matplotlib', 'inline')





# ## Problem: Selecting Elements using Logical Statements
# For portfolio 1 and portfolio 10, select the elements that are $<0$,
# $\geq 0$ and exactly equal to $0$. Next select the elements where both
# portfolios are less than $0$. 
# 










# ## Problem: Using `where`
# Use `where` to select the index of the elements in portfolio 5 that are
# negative. Next, use the `where` command in its two output form to determine
# which elements of the portfolio return matrix are less than -2%.










# ## Problem: Combining flow control
# For momentum portfolios 1 and 10, compute the length of the runs in the
# series. In pseudo code,
# 
# * Start at i=1 and define run(1) = 1
# * For i in 2,...,T, define run(i) = run(i-1) + 1 if 
#   $\textrm{sgn}\left(r_{i}\right)=\textrm{sgn}\left(r_{i-1}\right)$ else 1.
# 
# You will need to use `len` and `zeros`. 
# 
# 1. Compute the length longest run in the series and the index of the
#    location of the longest run. Was it positive or negative?
# 2. How many distinct runs lasted 5 or more days?







# ## Problem: Use `any` to find large losses
# 
# Use any to determine if any of the 10 portfolios experienced a loss
# greater than -5%.










# Use `all` and negation to do the same check as `any`.




# ## Exercises
# 
# ### Exercise: all and any
# Use all to determine the number of days where all of the portfolio returns
# were negative. Use any to compute the number of days with at least 1 negative
# return and with no negative returns (Hint: use negation (~ or `logical_not`)). 
