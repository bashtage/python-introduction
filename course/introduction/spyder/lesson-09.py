#!/usr/bin/env python
# coding: utf-8

# %%
# # Common DataFrame methods
#
# This lesson introduces the common `DataFrame` methods that
# we will repeatedly use in the course.
#
# This first cell load data for use in this lesson.

# %%
# Setup: Load prices
import pandas as pd

prices = pd.read_hdf("data/dataframes.h5", "prices")
sep_04 = pd.read_hdf("data/dataframes.h5", "sep_04")
goog = pd.read_hdf("data/dataframes.h5", "goog")
returns = prices.pct_change().dropna()
spy_returns = returns.SPY
aapl_returns = returns.AAPL
goog_returns = returns.GOOG


# %%
# ## Problem: Constructing portfolio returns
#
# Compute the return of a portfolio with weight $\frac{1}{3}$ in each security using
# multiplication (`*`) and `.sum()`.
#
# **Note**: You need to use the `axis` keyword for the sum.

# %%


# %%
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

# %%


# %%


# %%


# %%
# ## Problem: Compute Correlation
# Compute the correlation of the matrix of returns (`corr()`).

# %%


# %%
# ## Problem: Summing all elements
#
# Compute the sum of the columns of returns using `.sum()`. How is this related to the mean computed
# in the previous step?

# %%


# %%


# %%
# ## Problem: Maximum and Minimum Values
# Compute the minimum and maximum values of the columns of returns using the `min()` and `max()` commands.

# %%


# %%


# %%
# ## Problem: Rounding Up, Down and to the Closest Integer
#
# Rounding up is handled by ceil, rounding down is handled by floor and rounding to the closest
# integer is handled by round. Try all of these commands on 100 times returns. For example,
# ```python
# rounded = (100*returns).round()
# ```
#
# Use `ceil` and `floor` to round up and down, respectively.

# %%


# %%


# %%


# %%
# ## Exercises
#
# ### Exercise: Compute Quantiles
#
# Compute the 5%, 25%, 50%, 75% and 95% quantiles of momentum using the `quantile`
# method.
#

# %%
# Setup: Load data
import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)
mom_10 = momentum.mom_10


# %%


# %%
# ### Exercise: Sorting
#
# Use `sort_values` to sort momentum by the column `mom_10`. Verify that the
# sort was successful by looking at the minimum of a diff.

# %%


# %%


# %%
# ### Exercise: Sort Descending
#
# Use `sort_values` to sort momentum by by the column `mom_10` using a descending
# sort (see the help for `sort_values`). Verify the sort worked by looking at the maximum of
# a diff.

# %%


# %%


# %%


# %%


# %%
# ### Exercise: Get Number of Elements
#
# Use the `shape` property to get the number of observations in momentum. Use it
# again to get the number of columns.

# %%


# %%


# %%
# ### Exercise: Use `shift` to Compute Returns
#
# Compute the percentage change using only `shift`, division (`/`) and
# subtraction (`-`) on the `Series` `mom_10`. Verify that your result matches what `pct_change` produces.

# %%
