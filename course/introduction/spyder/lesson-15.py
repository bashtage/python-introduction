#!/usr/bin/env python
# coding: utf-8

#%%
# # Boolean Arrays
#
# This lesson covers:
#
# * Creating Boolean arrays
# * Combining Boolean arrays
# * `all` and `any`
#
# Begin by loading the data in momentum.csv.
#

#%%
# Setup: Load the momentum data

import numpy as np
import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)

print(momentum.head())

mom_01 = momentum["mom_01"]
mom_10 = momentum["mom_10"]
mom_05 = momentum["mom_05"]


#%%
# ## Problem: Boolean arrays
# For portfolios 1 and 10, determine whether each return is $<0$ (separately).

#%%


#%%
# ## Problem: Combining boolean arrays
# Count the number of times that the returns in both portfolio 1 and portfolio
# 10 are negative. Next count the number of times that the returns in portfolios
# 1 and 10 are both greater, in absolute value, that 2 times their respective
# standard deviations.

#%%


#%%


#%%
# ## Problem: Combining boolean arrays
# For portfolios 1 and 10, count the number of times either of the returns is $<0$.
#

#%%


#%%
# ## Problem: Count the frequency of negative returns
#
# What percent of returns are negative for each of the 10 momentum portfolios?

#%%


#%%
# ## Problem: Use `any` to find large losses
#
# Use any to determine if any of the 10 portfolios experienced a loss
# greater than -5%.

#%%


#%%


#%%


#%%
# Use `all` and negation to do the same check as `any`.

#%%


#%%
# ## Exercises
#
# ### Exercise: all and any
# Use `all` and `sum` to count the number of days where all of the portfolio returns
# were negative. Use `any` to compute the number of days with at least 1 negative
# return and with no negative returns (Hint: use negation (~ or `logical_not`)).

#%%


#%%


#%%


#%%
# ### Exercise: Count Extreme Days
#
# Count the number of days where each of the portfolio returns is less than the
# 5% quantile for the portfolio. Also report the fraction of days where all are in their
# lower 5% tail.

#%%


#%%
