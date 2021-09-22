#!/usr/bin/env python
# coding: utf-8

#%%
# # Conditional Statements
#
# * `if`-`elif`-`else` blocks

#%%
# ## Problem: Print value if negative
#
# Draw a standard normal value using `np.random.standard_normal` and print the
# value if it is negative.
#
# **Note**: Rerun the cell a few time to see different output.

#%%


#%%
# ## Problem: Print different messages based on value
#
# Draw a standard normal value and print "Positive" if it is positive
# and "Negative" if not.

#%%


#%%
# ## Problem:
#
# Draw a standard t random variable with 2 degrees of freedom using
# `np.random.standard_t(2)` and print "Negative Outlier" if less than -2,
# "Positive Outlier" if larger than 2, and "Inlier" if between -2 and 2.

#%%


#%%
# ## Exercises
#
# ### Exercise: Classify two points
#
# Generate two standard normal values `x` and `y` using
# two calls to `rs.standard_normal()`. Use an `if`-`elif`-`else`
# clause to print the quadrant they are in.  The four quadrants are
# upper right, upper left, lower left and lower right.
#

#%%


#%%


#%%


#%%
# ### Exercise: Generate a contaminated normal
#
# Generate a uniform using `u = rs.sample()`. Using this value and an
# `if`-`else` clause, generate a contaminated normal which is a draw from a
# $N(0,1)$ ($N(\mu,sigma^2)$) if $u<0.95$ or a draw from a $N(0,10)$ otherwise.
# Use `rs.normal` to generate the normal variable.

#%%
