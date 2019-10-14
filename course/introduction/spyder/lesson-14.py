#!/usr/bin/env python
# coding: utf-8

#%%
# # Logical Operators
# 
# This lesson covers:
# 
# * Basic logical operators 
# * Compound operators 
# 

#%%
# Setup: Reproducible random numbers

import numpy as np
rs = np.random.RandomState(20000101)


#%%
# ## Problem: Basic Logical Statements
# 
# Create the variables (in order)
# 
# * `x` as `rs.sample()`, a uniform on $[0, 1)$
# * `y` as `rs.standard_normal()`, a standard normal ($N(0,1)$)
# * `z` as `rs.randint(1, 11)`, a uniform ranomd integer on $[1, 2,\ldots, 10]$
# 
# Check whether each of these are above their expected value.

#%%


#%%


#%%
# ## Problem: Using comparison operators
# 
# 1. Check if `z` if 7
# 2. Check is `z` is not 5
# 3. Check if `z` is greater than or equal to 9

#%%


#%%
# ## Problem: Combining booleans 
# 
# 1. Determine if $2\leq z < 8$
# 2. Determine if $z < 2 \cup z \geq 8$ using `or`
# 3. Rewrite 2 using `not` and your result from 1.

#%%

