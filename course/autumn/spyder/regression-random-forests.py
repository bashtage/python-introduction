#!/usr/bin/env python
# coding: utf-8

#%%
# # Regression: Random Forests
# 
# 
# **Functions**
# 
# `sklearn.ensemble.RandomForestRegressor`, `sklearn.model_selection.GridSearchCV`, `sklearn.ensemble.GradientBoostingRegressor`
# 
# This notebook continues the example from the Best Subset and Stepwise Regression notebook that constructs a tracking portfolio.
# 
# **Warning**: This notebook is simply an example of how to use these methods. In general tree-based models are terrible choices for tracking portfolio construction since the final model is not a weighted combination of the returns, but instead depends on non-linear transformation of the returns. This makes implementation of a tree-based estimator virtually impossible. 

#%%


#%%
# ## Data
# 
# Here we use the same problem (portfolio tracking) and data that was used in the Best Subset and Stepwise regression notebook.

#%%


#%%
# We first show the OLS in-sample SSE as a benchmark value.

#%%


#%%
# ## Random Forests

#%%
# Random Forests fit ensembles of trees (combinations) using a random sample of the regressors in each.  Here we fit a default Random Forest where we use the $\sqrt{p}$ rule for feature selection within each tree. The should reduce the correlation between trees.
# 
# The in-sample SSE is very good and much smaller than the in-sample SSE of OLS.

#%%


#%%
# The out-of-sample SSE, however, is quite a bit worse than OLS.  Tree-based models are not good models for tracking portfolio construction.

#%%


#%%
# `GridSearchCV` allows us to compute the cross-validated score of a model for a combination of input parameters. This method is similar to writing a number of loops across each of the parameters and then cross-validating the model for each distinct combination.  
# 
# The key input to `GridSearchCV` is a dictionary where the keys are model parameter names and the values are the values that should be considered in the search.  The model is then automatically cross-validated for all of combinations of the parameters. 
# 
# **Note**: This cell may run of an extended period, depending on your system.

#%%


#%%
# The best estimator in the sense of minimizing the score function (negative MSE here) is available using the `best_estimator_` attribute. This is a `RandomForestRegressor` with the CV-optimized parameters. This estimator can then be fit to the data.

#%%


#%%
# The in-sample SSE is very good, and is slightly better than the naive attempt.

#%%


#%%
# Note that the cross-validated sse is related to the negative MSE usign the relationship
# $$ Neg MSE = -\frac{SSE_{xv}}{n} $$
# 
# The values are stored in a dictionary `gscv.cv_results_` using the key `"mean_test_score"`.  We can convert these to cross-validated SSE for comparison with other methods. These are all higher than what we saw with regression methods.

#%%


#%%
# `cv_results_` also contains the parameters used in each configuration. Here we can build a `DataFrame` that examines the better parameterizations by merging these values with the $SSE_{xv}$ and sorting.  We see that the best configurations always used `"sqrt"` for `max_features`, and the 500 consistently outperformed 250 or 1000 estimators. 

#%%


#%%
# Finally we can compute the OOS SSE using the `predict` method with the out-of-sample data. This value is poor when compared to OLS.  This indicates (not surprisingly) that tree-based methods are not good ways to fit financial return data.

#%%


#%%
# ## Boosting
# 
# Boosting is often a better alternative to Random Forests sine it limits tree depth, and in turn, variable interactions.
# 
# Here we fit a default boosted regression tree using `GradientBoostingRegressor`.  it is always a good idea to set `random_state` to ensure results are reproducible. We compute the OOS SSE and see that the default parameters perform well when compared to either Random Forest.

#%%


#%%
# Boosted models can be tuned like any other approach.  Here we use `GridSearchCV` again to search for good choices of the learning rate ($\lambda$ in the notes), the number of estimators ($B$ in the notes), and the `max_leaf_nodes` ($d$ in the notes).
# 
# **Note**: This cell can take a while to run, depending on your machine.

#%%


#%%
# The preferred configuration has a large number of estimators with a relatively low learning rate and small trees.

#%%


#%%
# When we look at the top performing estimators, we see that small trees combined, slow learning and many estimators consistently perform best.

#%%


#%%
# We can generate the out-of-sample SSE for the optimized GBR. We see that while it is substantially improved over what we found with a Regression Tree, it is still 15% worse then what plain OLS achieves.

#%%

