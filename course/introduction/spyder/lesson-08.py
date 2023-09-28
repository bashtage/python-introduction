#!/usr/bin/env python
# coding: utf-8

# %%
# # Using DataFrames
#
# This lesson introduces:
#
# * Computing returns (percentage change)
# * Basic mathematical operations on DataFrames
#
# This first cell load data for use in this lesson.

# %%
# Setup: Load prices
import pandas as pd

prices = pd.read_hdf("data/dataframes.h5", "prices")
sep_04 = pd.read_hdf("data/dataframes.h5", "sep_04")
goog = pd.read_hdf("data/dataframes.h5", "goog")


# %%
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
# spy_returns = returns["SPY"]
# ```

# %%


# %%


# %%


# %%
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

# %%


# %%
# ## Basic Mathematical Operations
#
# |  Operation            | Symbol | Precedence |
# |:----------------------|:------:|:----------:|
# | Parentheses           | ()     | 4          |
# | Exponentiation        | **     | 3          |
# | Multiplication        | *      | 2          |
# | Division              | /      | 2          |
# | Floor division        | //     | 2          |
# | Modulus               | %      | 2          |
# | Matrix multiplication | @      | 2          |
# | Addition              | +      | 1          |
# | Subtraction           | -      | 1          |
#
# **Note**: Higher precedence operators are evaluated first, and ties are
# evaluated left to right.
#
#
# ## Problem: Scalar Operations
# 1. Add 1 to all returns
# 2. Square the returns
# 3. Multiply the price of Google by 2.
# 4. Extract the fractional return using floor division and modulus

# %%


# %%


# %%


# %%


# %%


# %%
# ## Problem: Addition of Series
# Add the returns on SPY to those of AAPL
#

# %%


# %%
# ## Problem: Combining methods and mathematical operations
# Using only basic mathematical operations compute the
# correlation between the returns on AAPL and SPY.

# %%


# %%
# ## Problem: Addition of DataFrames
# Construct a `DataFrame` that only contains the SPY column from returns
# and add it to the return `DataFrame`

# %%


# %%
# ## Problem: Non-conformable math
#
# Add the prices in `sep_04` to the prices of `goog`. What happens?

# %%


# %%
# ## Problem: Constructing portfolio returns
# Set up a 3-element array of portfolio weights
#
# $$w=\left(\frac{1}{3},\,\frac{1}{3}\,,\frac{1}{3}\right)$$
#
# and compute the return of a portfolio with weight $\frac{1}{3}$ in each security.
#

# %%


# %%
# ## Exercises
#
# ### Exercise: Combine math with function
#
# Add 1 to the output of `np.arange` to produce the sequence 1, 2, ..., 10.

# %%


# %%
# ### Exercise: Understand pandas math
#
# Use the `Series` and `DataFrame` below to compute the sums
#
# * `a+b`
# * `a+c`
# * `b+c`
# * `a+b+c`
#
# to understand how missing values are treated by pandas

# %%
# Setup: Data for exercise
import numpy as np
import pandas as pd

rs = np.random.RandomState(19991231)

idx = ["A", "a", "B", 3]
columns = ["A", 1, "B", 3]
a = pd.Series([1, 2, 3, 4], index=idx)
b = pd.Series([10, 9, 8, 7], index=columns)
values = rs.randint(1, 11, size=(4, 4))
c = pd.DataFrame(values, columns=columns, index=idx)


# %%


# %%


# %%


# %%


# %%
# ### Exercise: Math with duplicates
#
# Add the Series `d` to `a` to see what happens with delays.

# %%
# Setup: Data for exercise

d = pd.Series([10, 101], index=["A", "A"])


# %%
