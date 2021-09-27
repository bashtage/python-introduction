#!/usr/bin/env python
# coding: utf-8

#%%
# # Custom Functions
#
# This lesson covers:
#
# * Writing a custom function

#%%
# ## Problem: Writing a Custom Function
# Custom functions will play an important role later in the course when
# estimating parameters. Construct a custom function that takes two arguments,
# mu and sigma2 and computes the likelihood function of a normal random variable.
#
# $$f(x;\mu,\sigma^{2})=\frac{1}{\sqrt{2\pi\sigma^{2}}}\exp\left(-\frac{(x-\mu)^{2}}{2\sigma^{2}}\right)$$
#
# Use `def` to start the function and compute the likelihood of:
#
# $$x=0,\mu=0,\sigma^{2}=1.$$
#
# The text in the triple quotes is the docstring which is optional.

#%%


#%%


#%%


#%%
# ## Exercises
#
# ### Exercise: Custom Function
#
# Write a function named summary_stats that will take a single input, x,
# a DataFrame and return a DataFrame with 4 columns and as many rows as
# there were columns in the original data where the columns contain the mean,
# standard deviation, skewness and kurtosis of x.
#
# Check your function by running
# ```python
# summary_stats(momentum)
# ```

#%%
# Setup: Load the momentum data
import pandas as pd

momentum = pd.read_csv("data\momentum.csv", index_col="date", parse_dates=True)


#%%


#%%
# Test your function using the momentum data in the next cell.

#%%


#%%
# ### Exercise: Custom Function
#
# Change your previous function to return 4 outputs, each a pandas Series for the mean,
# standard deviation, skewness, and the kurtosis.
#
# Returning multiple outputs uses the syntax
# ```python
# return w, x, y, z
# ```
#
# Test your function using the momentum data.

#%%


#%%
# Test your function using the momentum data in the next cell.

#%%
