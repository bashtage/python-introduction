#!/usr/bin/env python
# coding: utf-8

# %%
# ## Linear Regression: Ridge Regression and LASSO
#
# **Functions**
#
# `sklearn.linear_model.RidgeCV`, `sklearn.linear_model.LassoCV`, `sklearn.preprocessing.StandardScaler`
#

# %%


# %%
# ### Exercise 49
#
# Standardize the value-weighted-market return data and the 12 industry portfolios by their standard deviation. You should _not_ remove the mean since we want to match the mean in the tracking portfolio.

# %%


# %%
# ### Exercise 50
#
# Select the optimal tuning parameter in a LASSO and estimate model parameters for the tracking error minimizing portfolio using the standardized data.

# %%


# %%
# ### Exercise 51
#
# Transform the estimated LASSO coefficients back to the scale of the original, non-standardized data.

# %%


# %%
# ### Exercise 52
#
# Select the optimal tuning parameter in a Ridge regression and estimate model parameters for the tracking error minimizing portfolio using the standardized data.

# %%


# %%
# ### Exercise 53
#
# Transform the estimated Ridge regression coefficients back to the scale of the original, non-standardized data.

# %%


# %%
# ### Exercise 54
#
# Compare the parameter estimates from the LASSO and Ridge regression to those from OLS in a plot. Use the original, non-standardized data.

# %%


# %%
# ### Exercise 55
#
# Use scikit-learn to scale the standardize the data by changing the scale but not the mean.
#

# %%


# %%
# ### Exercise 56
#
# Use the scikit-learn scaler to compute the predicted in-sample values using the Ridge ridge regression.

# %%


# %%
# ### Exercise 57
#
# Use the scalar from scikit-learn to produce out-of-sample forecasts of the two shrinkage estimators and OLS and evaluate the out-of-sample SSE.
#

# %%


# %%
# ### Exercise 58
#
# Directly produce out-of-sample forecasts of the two shrinkage estimators and OLS and evaluate the out-of-sample SSE without using scikit-learn.
#

# %%
