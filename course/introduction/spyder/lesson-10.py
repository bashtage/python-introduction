#!/usr/bin/env python
# coding: utf-8

# # Accessing Elements in NumPy Arrays
# 
# This lesson covers:
# 
# * Accessing specific elements in NumPy arrays
# 
# Accessing elements in an array or a DataFrame is a common task. To begin this lesson, clear the
# workspace set up some vectors and a $5\times5$ array. These vectors and matrix will make it easy
# to determine which elements are selected by a command.
# 
# 
# Using `arange` and `reshape` to create 3 arrays:
# 
# * 5-by-5 array `x` containing the values 0,1,...,24 
# * 5-element, 1-dimensional array `y` containing 0,1,...,4
# * 5-by-1 array `z` containing 0,1,...,4
# 










# ## Zero-based indexing
# Python indexing is 0 based so that the first element has position `0`, the second has position `1`
# and so on until the last element has position `n-1` in an array that contains `n` elements in
# total.
# 
# ## Problem: Scalar selection
# Select the number 2 in all three, `x`, `y`, and `z`.
# 
# 
# **Question**:  Which index is rows and which index is columns?










# ## Problem: Scalar selection of a single row
# 
# Select row 2 in `x` and `z` using a single integer value.
#  
# **Question**: What is the dimension of `x` and the second row of `x`













# ## Problem: Slice selection of a single row
# 
# Use a slice to select the 2nd row of `x` and the 2nd element of `y` and `z`.
# 
# **Question**: What are the dimension selections?










# ## Problem: List selection of a single row
# 
# Use a list to select the 2nd row of `x` and the 2nd element of `y` and `z`.
# 
# **Question**: What are the dimension selections?










# ## Problem: Selecting a single Column
# Select the 2nd column of x using a scalar integer, a slice and a list.
# 
# **Question**: What the the dimensions of the selected elemets? 







# ## Problem: Selecting Specific Rows or Columns
# 1. Select the 2nd and 3rd columns of x using a slice.
# 2. Select the 2nd and 4th rows of x using both a slice and a list. 
# 3. Combine these be combined to select columns 2 and 3 and rows 2 and 4. 










# ## Problem: Use `ix_` to select rows and columns using lists
# Use `ix_` to select the 2nd and 4th rows and 1st and 3rd columns of `x`.







# ## Problem: Convert a DataFrame to a NumPy array
# 
# Use  `.to_numpy` to convert a DataFrame to a NumPy array.

# Setup: Create a DataFrame
import pandas as pd
import numpy as np

names = ["a", "b", "c", "d", "e"]
x = np.arange(25).reshape((5,5))
x_df = pd.DataFrame(x, index=names, columns=names)
print(x_df)





# ## Problem: Use `np.asarray` to convert to an array
# 
# Use  `np.asarray` to convert a DataFrame toa NumPy array.



