#!/usr/bin/env python
# coding: utf-8

#%%
# ## Linear Regression: Model Selection and Cross-Validation
# 
# Functions
# 
# `RandomState.permute`, `sm.OLS`, `set`, `scipy.random.norm.ppf`, `np.linspace`, `np.mean`
# 
# ### Exercise 39
# Four portfolios we have been looking at, and considering all 8 sets of
# regressors which range from no factor to all 3 factors, which model is preferred
# by AIC, BIC, GtS and StG?

#%%


#%%


#%%


#%%
# #### Discussion
# 
# For each of the portfolios, we start with a list of included variables 
# that includes all three factors. We can then use a loop to see if any
# of the included variables have insignificant t-stats.  We first create a
# temporary set of regressors that uses the factors are are in `included`.
# We can then check if any of the t-stats are less than our critical value
# that is defined above.  If one is less than the value, we need to drop the
# variable. We sort the absolute t-stats so that the minimum is first,
# and then get the variable name from the index. Finally, we use `.remove`
# to remove this name from the list of included variables. 
# 
# If no t-stat is less than our critical value, we can call `break` which 
# terminates the loop early. 

#%%


#%%
# ### Exercise 40
# Cross-validation is a method of analyzing the in-sample forecasting ability of a
# cross-sectional model by using $\alpha\%$ of the data to estimate the model and
# then measuring the fit using the remaining $100-\alpha\%$. The most common forms
# are 5- and 10-fold cross-validation which use $\alpha=20\%$ and $10\%$, respectively.
# k-fold cross validation is implemented by randomly grouping the data into
# k-equally-sized groups, using k-1 of the groups to estimate parameters, and
# then evaluating using the bin that was held out. This is then repeated so that
# each bin is held out.
# 
# 1. Implement cross-validation using the 5- and 10-fold methods for all 8 models.
# 2. For each model, compute the full-sample sum of squared errors as well as the
#    sum-of-squared errors using the held-out sample. Note that all data points
#    will appear exactly once in both of these sum or squared errors. What happens
#    to the cross-validated $R^{2}$ when computed on the held out sample when compared
#    to the full-sample $R^{2}$? (k-fold cross validated SSE by the TSS).

#%%

