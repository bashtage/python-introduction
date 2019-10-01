#!/usr/bin/env python
# coding: utf-8

# # Logical Operators
# 
# This lesson covers:
# 
# * Basic logical operators 
# * Compound operators 
# 
# Begin by loading the data in momentum.csv.

# Setup: Load the momentum data

import pandas as pd

momentum = pd.read_csv('data/momentum.csv', index_col='date', parse_dates=True)

print(momentum.head())

mom_01 = momentum['mom_01']
mom_10 = momentum['mom_10']
mom_05 = momentum['mom_05']


# ## Problem: Basic Logical Statements
# 
# For portfolio 1 and portfolio 10, count the number of elements that are $<0$, $\geq0$, and exactly
# equal to 0. Next count the number of times that the returns in portfolio 5 are greater, 
# in absolute value, that 2 times the standard deviation of the returns in that portfolio. 
# 
# 







# ## Problem: Compound Statements
# Count the number of times that the returns in both portfolio 1 and portfolio 10 are negative. 
# Next count the number of times that the returns in portfolios 1 and 10 are both greater, in 
# absolute value, that 2 times their respective standard deviations. 






