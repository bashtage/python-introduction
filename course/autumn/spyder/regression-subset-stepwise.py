#!/usr/bin/env python
# coding: utf-8

#%%
# ## Linear Regression: Best Subset and Stepwise Regression
#
# **Functions**
#
# `np.linalg.lstsq`, `sklearn.model_selection.cross_val_score`, `sklearn.linear_model.LinearRegression`, `sklearn.model_selection.KFold`

#%%


#%%
# ### Exercise 41
# Download data from [Ken French's website](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/) on the VWM and the 12 industry portfolios. Reformat both data sets so that they has a `DatetimeIndex`.
#

#%%


#%%
# ### Exercise 42
#
# Use Best Subset Regression with cross-validation to select the weights of a tracking portfolio where the industry portfolios are used to track the value-weighted-market. Use data until the end of 2014. A tracking portfolio is a portfolio that replicates a portfolio using other assets. The weights can be estimated using a regression model excludes a constant.
#
# $$ R_{i,p} = \beta_1 R_{i,1} + \beta_2 R_{i,2} + \ldots + \beta_k R_{i,k} + \epsilon_{i} $$
#
# where $R_{i,j}$ are returns on the assets used to construct the tracking portfolio. The constant is excluded since the portfolio should track both the shock and match the mean return. OLS minimizes the variance of the tracking error (in-sample).

#%%


#%%
# ### Exercise 43
#
# Select the best tracking portfolio using Forward Stepwise Regression.

#%%


#%%
# ### Exercise 44
#
# Use Backward Stepwise Regression to select the tracking portfolio.

#%%


#%%
# ### Exercise 45
#
# Using scikit-learn to cross-validate the Backward Stepwise selected models.
#

#%%


#%%
# ### Exercise 46
#
# Repeat the cross-validation using scikit-learn using randomly selected values in each block.

#%%


#%%
# ### Exercise 47
#
# Evaluate the models selected using the sample that was _not_ used in fitting to assess the out-of-sample performance based on SSE.

#%%


#%%
# ### Exercise 47
#
# Compute the in-sample and out-of-sample $R^2$ for the selected models.
#
# The out-of-sample $R^2$ defined as
#
# $$ 1 - \frac{SSE_{OOS}}{TSS_{OOS}} $$
#
# where the $SSE_{OOS}$ is the SSE using the predicted values and the $TSS_{OOS}$ is the TSS computed using the in-sample value (without demeaning since the models we are fitting do not include a constant). **Note**: If a model does not contain a constant, the $TSS_{OOS}$ is _not_ demeaned.

#%%


#%%
# ### Exercise 48
#
# Use scikit-learn to produce out-of-sample fits and compute the out-of-sample SSE.  Verify this value is the same as you found previously.

#%%
