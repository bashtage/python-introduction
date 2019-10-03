#!/usr/bin/env python
# coding: utf-8

# # Final Exam
# 
# This self-grading notebook serves as a final exam for the introductory course.
# If you have grasped the contents of the course, you should be able to complete
# this exam. 
# 
# It is essential that you answer each cell by assigning the solution to `QUESTION_#`
# where `#` is the question number.  
# 
# We will start with a warm-up question that is already answered.
# 
# ## Question 0
# 
# Create a 3-element 1-dimensional array containing the values [1,1,1]
# 
# _Note_: This answer is not assessed.

# Setup: The solution is used as a model
import numpy as np

QUESTION_0 = np.ones(3) 


# ## Question 1
# 
# Construct the correlation matrix
# 
# $$\left[\begin{array}{ccc} 1 & 0.2 & 0.5 \\ 0.2 & 1 & 0.8 \\ 0.5 & 0.8 & 1 \end{array}\right]$$
# 
# as a NumPy array.




# ## Question 2
# 
# Construct the correlation matrix
# 
# $$\left[\begin{array}{ccc} 1 & 0.2 & 0.5 \\ 0.2 & 1 & 0.8 \\ 0.5 & 0.8 & 1 \end{array}\right]$$
# 
# as a DataFrame with columns and index both equal to `['A', 'B', 'C']`. 




# ## Question 3
# 
# Load the momentum data in the CSV file `momentum.csv`, set the column `date` 
# as the index, and ensure that `date` is a `DateTimeIndex`.




# ## Question 4
# 
# Construct a DataFrame using the data loaded in the previous question
# that contains the returns from momentum portfolio 5 in March and April 2016.
# 




# ## Question 5
# 
# What is the standard deviation of the data:
# 
# $$ 1, 3, 1, 2,9, 4, 5, 6, 10, 4 $$
# 
# **Note** Use 1 degree of freedom in the denominator.




# ## Question 6
# 
# Compute the correlation matrix of momentum portfolios 1, 4, 6, and 10 as a DataFrame
# where the index and columns are the portfolio names (e.g., 'mom_01') in the order
# listed above.




# ## Question 7
# 
# Compute the percentage of returns of each of the 10 momentum portfolios
# that are outside of the interval 
# 
# $$ [\hat{\mu} - \hat{\sigma}, \hat{\mu} + \hat{\sigma}]$$
# 
# where $\hat{\mu}$ is the mean and $\hat{\sigma}$ is the standard deviation computed using
# 1 dof.  The returned variable must be a `Series` where the index is the portfolio
# names ordered from 1 to 10.
#  




# ## Question 8
# 
# Import the data the data in the sheet `question 8` in `final-exam.xlsx` into
# a DataFrame where the index contains the dates and variable name is the column
# name.




# ## Question 9
# 
# Enter the DataFrame in the table below and save it to HDF with the key 'question9'. The answer to
# this problem must be the full path to the hdf file. The values in
# index should be the DataFrame's index.
# 
# | index | data |
# | :---- | :--- |
# |  A    | 6.0  |
# |  E    | 2.7  |
# |  G    | 1.6  |
# |  P    | 3.1  |
# 
# **Note**: If you want to get the full path to a file saved in the current directory, 
# you can use
# 
# ```python
# import os
# 
# file_name = 'my_file_name'
# full_path = os.path.join(os.getcwd(), file_name)
# ```




# ## Question 10
# 
# Compute the cumulative return on a portfolio the longs mom_10 and shorts mom_01. The
# first value should be `1 + mom_10.iloc[0] - mom_01.iloc[0]`. The second cumulative
# return should be the first return times `1 + mom_10.iloc[1] - mom_01.iloc[1]`, and
# so on.  The solution must be a Series with the name 'momentum_factor' and index
# equal to the index of the momentum DataFrame. 
# 
# **Note**: The data in the momentum return file is in percentages, i.e., a return of
# 4.2% is recorded as 4.2. 




# ## Question 11
# 
# Write a function named QUESTION_11 that take 1 numerical input `x` and returns:
# 
# * $exp(x)$ is x is less than 0
# * $log(1+x)$ if `x` is greater than or equal to 0
# 




# ## Question 12
# 
# Produce a scatter plot of the momentum returns of portfolios 1 (x-axis) and 10 using only
# data in 2016.  Set the x limits and y limits to be tight so that the lower bound is the 
# smallest return plotted and the upper bound is the largest return plotted. Use the 'darkgrid'
# theme from seaborn.  Assign the **figure** handle to QUESTION_12.
#  




# ## Question 13
# 
# Compute the excess kurtosis of daily, weekly (using Friday and the end of the week) and monthly 
# returns on the 10 momentum portfolios using the pandas function `kurt`. The solution must be a
# DataFrame with the portfolio names as the index ordered form 1 to 10 and the sampling frequencies,
# 'daily', 'weekly', or 'monthly' as the columns (in order). When computing weekly or monthly returns
# from daily data, use the sum of the daily returns.  




# ## Question 14
# 
# Simulate a random walk using 100 normal observations from a
# NumPy `RandomState` initialized with a seed of `19991231`.




# ## Question 15
# 
# Defining 
# 
# ```
# import numpy as np
# 
# cum_momentum = np.cumprod(1 + momentum / 100)
# ```
# 
# compute the ratio of the high-price to the low price in each month.  The solution
# should be a DataFrame where the index is the last date in each month and the columns
# are the variables names.
#  




# ## Question 16
# 
# Simulate 100 observations from the model
# 
# $$ y_i = 0.2 + 1.2 y_{i-1} - 0.2 y_{i-2} + \epsilon_i$$
# 
# where $\epsilon_i$ is a standard normal shock.  Set $y_0=\epsilon_0$ and
# $y_1=\epsilon_0 + \epsilon_1$. The solution should be a 1-d NumPy array with 100 elements. Use
# a RandomState with a seed value of 19991231.




# ## Question 17
# What is the ratio of the largest eigenvalue to the smallest eigenvalue 
# of the correlation matrix of the 10 momentum returns? 
# 
# **Note**: This is called the condition number of a matrix and is a measure of
# how closely correlated the series are. You can compute the eigenvalues from
# the correlation matrix using `np.linalg.eigs`.  See the help of this function
# for more details. 




# ## Question 18
# 
# Write a function that takes a single input 'x' and return the string
# "The value of x is " and the value of x. For example, if x is 3.14,
# then the returned value should be "The value of x is 3.14". The function name
# must be QUESTION_18.




# ## Question 19
# 
# Compute the percentage of days where all 10 returns are positive and subtract the
# percentage of days where all 10 momentum returns are negative on the same day.




# ## Question 20
# 
# Write the function `QUESTION_20` that will take a single input `s`, which is a string
# and will return a Series that counts the number of times each letter in `s` appears in `s`
# _without_ regard to case. Do not include spaces.  Ensure the Series returned as its index sorted.
# 
# **Hints**:
# 
# * Have a look at `value_counts` for a pandas `Series`.
# * You can iterate across the letters of a string using
# 
# ```
# some_string = 'abcdefg'
# for letter in some_string:
#     do somethign with letter...
# ```
# * `str.lower` can be used to get the lower case version of a string



