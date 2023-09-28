#!/usr/bin/env python
# coding: utf-8

# %%
# ## Regression: Tree-based Methods
#
#
# **Functions**
#
# `sklearn.ensemble.RandomForestRegressor`, `sklearn.model_selection.GridSearchCV`, `sklearn.ensemble.GradientBoostingRegressor`

# %%


# %%
# ### Exercise 59
#
# Load the portfolio tracking data and compute the in- and out-of-sample SSE for OLS.

# %%


# %%
# ### Exercise 60
#
# Fit a default Random Forest in a reproducible manner to the portfolio tracking data and compute the in- and out-of-sample SSE.
#
# **Warning**: This exercise is simply an example of how to use these methods. In general tree-based models are terrible choices for tracking portfolio construction since the final model is not a weighted combination of the returns, but instead depends on non-linear transformation of the returns. This makes implementation of a tree-based estimator virtually impossible.

# %%


# %%
# ### Exercise 61
#
# Optimize the key tuning parameters of the Random Forest using cross-validation and compute the out-of-sample SSE of the preferred model.

# %%


# %%
# ### Exercise 62
#
# Boosting is often a better alternative to Random Forests sine it limits tree depth, and in turn, variable interactions. Fit a default boosted regression tree to the portfolio tracking data, and compute the out-of-sample SSE.

# %%


# %%
# ### Exercise 63
#
# Optimize the key parameters of the boosted regression tree using cross-validation.

# %%


# %%
# ### Exercise 64
#
# Compute the out-of-sample SSE for the selected boosted regression tree.

# %%
