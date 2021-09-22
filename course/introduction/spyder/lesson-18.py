#!/usr/bin/env python
# coding: utf-8

#%%
# # Logic and Loops
#
# This lesson covers:
#
# * Mixing logic and loops

#%%
# Setup: Load the momentum data

import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)

mom_01 = momentum.mom_01
print(momentum.head())


#%%
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

#%%


#%%
# Plot the two random walks using the code.  We will cover data visualization
# in a later lesson.
#
# ```python
# %matplotlib inline
# import matplotlib.pyplot as plt
# plt.plot(y)
# plt.plot(z)
# plt.legend(["y", "z"])
# ```

#%%


#%%
# ## Problem: Simulate the asymmetric random walk without an `if`-`then`
#
# Use boolean multiplication to simulate the same random walk without using
# an `if`-`then` statement.

#%%


#%%
# Setup: Plot the data
from IPython import get_ipython

get_ipython().run_line_magic("matplotlib", "inline")

import matplotlib.pyplot as plt

plt.rc("figure", figsize=(16, 6))  # Improve figure size
plt.rc("font", size=14)  # Improve figure size


#%%


#%%
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

#%%


#%%
# Plot the runs using
#
# ```python
# %matplotlib inline
#
# import matplotlib.pyplot as plt
# plt.plot(run)
# ```

#%%


#%%
# ## Exercises
#
# ### Exercise: Simulate a Process with Heteroskedasticity
#
# Simulate 100 observations of a time series with heteroskedasticity
# that follows a random walk of the form:
#
# $$ y_t = y_{t-1} + \sigma_t \epsilon_t $$
#
# where $\epsilon_t\sim N(0,1)$, $y_0=0$ and $\sigma_t$ is:
#
# * 0.5 if the 0 of the past 3 shocks are negative
# * 1 if 1 of the past 3 shocks are negative
# * 2 if 2 of the past 3 shocks are negative
# * 6 if 3 of the past 3 shocks are negative
#
# Plot the result.
#
# **Notes**
#
# * When generating the first 3 values, treat $\epsilon_{-1}$, $\epsilon_{-2}$ and
#   $\epsilon_{-3}$ as 0 (non-negative).
# * Re-run the simulation to see different paths.
#

#%%


#%%
