#!/usr/bin/env python
# coding: utf-8

# %%
# # Logical Operators
#
# This lesson covers:
#
# * Basic logical operators
# * Compound operators
#

# %%
# Setup: Reproducible random numbers

import numpy as np

rs = np.random.RandomState(20000101)


# %%
# ## Problem: Basic Logical Statements
#
# Create the variables (in order)
#
# * `x` as `rs.random_sample()`, a uniform on $[0, 1)$
# * `y` as `rs.standard_normal()`, a standard normal ($N(0,1)$)
# * `z` as `rs.randint(1, 11)`, a uniform random integer on $[1, 2,\ldots, 10]$
#
# Check whether each of these are above their expected value.

# %%


# %%


# %%
# ## Problem: Using comparison operators
#
# 1. Check if `z` is 7
# 2. Check is `z` is not 5
# 3. Check if `z` is greater than or equal to 9

# %%


# %%
# ## Problem: Combining booleans
#
# 1. Determine if $2\leq z < 8$
# 2. Determine if $z < 2 \cup z \geq 8$ using `or`
# 3. Rewrite 2 using `not` and your result from 1.

# %%


# %%
# ## Exercises

# %%
# Setup: Data for Exercise
import numpy as np

rs = np.random.RandomState(19991213)

# Like range, lower included, upper excluded
# u in (0, 1, 2, ..., 5)
u = rs.randint(0, 6)
# v in (-2, -1, 0, 1, 2)
v = rs.randint(-2, 3)


# %%


# %%
# ### Exercise
# Is the product $uv$ 0 and only one of $u$ and $v$ is 0?

# %%


# %%


# %%
# ### Exercise
#
# Write three logical statements that will determine if $0\leq u \leq 2$ and $0\leq v \leq 2$.

# %%


# %%


# %%
