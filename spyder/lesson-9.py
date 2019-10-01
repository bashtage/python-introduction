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
# ## Zero-based indexing
# Python indexing is 0 based so that the first element has position `0`, the second has position `1`
# and so on until the last element has position `n-1` in an array that contains `n` elements in
# total.
# 
# ## Problem: Picking an Element out of a Matrix
# 1. Select the third element of all three, x, y, and z. 
# 2. Select the 11$^{\text{th}}$ element of x.
# 3. Using double index notation, select the (0,2) and the (2,0) element of x.
# 
# **Issues to ponder**
# 
# * Which index is rows and which index is columns?
# * Does NumPy count across first then down or down first then across? 













# ## Problem: Selecting Entire Rows
# 1. Select the 2nd row of x using the colon (:) operator.
# 2. Select the 2nd element of z and y using the same syntax.
# 
# **Issues to ponder**
# 
# * What happens to the output in each case? 
# 




# ## Problem: Selecting Entire Columns
# Select the 2nd column of x using the colon (:) operator. 







# ## Problem: Selecting Specific Rows or Columns
# 1. Select the 2nd and 3rd columns of x using the colon (:) operator.
# 2. Select the 2nd and 4th rows of x. 
# 3. Combine these be combined to select columns 2 and 3 and rows 2 and 4. 










# ## Problem: Use `ix_` to select arbitrary rows and columns
# Use `ix_` to select the 2nd and 4th rows and 1st and 3rd columns of `x`.







# ## Problem: Convert a DataFrame to a NumPy array
# 
# Use  `.to_numpy` to convert a DataFrame toa NumPy array.




# ## Problem: Use `np.asarray` to convert to an array
# 
# Use  `.to_numpy` to convert a DataFrame toa NumPy array.



