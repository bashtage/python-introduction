#!/usr/bin/env python
# coding: utf-8

#%%
# ## Linear Regression: Ridge Regression and LASSO
# 
# **Functions**
# 
# `sklearn.linear_model.RidgeCV`, `sklearn.linear_model.LassoCV`, `from sklearn.preprocessing.StandardScaler`
# 
# This notebook continues the example from the Best Subset and Stepwise Regression notebook that constructs a tracking portfolio.

#%%


#%%
# ## Data
# 
# Here we use the same problem (portfolio tracking) and data that was used in the Best Subset and Stepwise regression notebook.

#%%


#%%
# ## Standardizing Data
# 
# We standardize the data by dividing by the the standard deviation. Note that we do not remove the mean since the portfolio tracking problem excludes an intercept.  The transformed data is then
# 
# $$ \tilde{X} = \frac{X - 0}{\hat{\sigma}} $$
# 
# where the mean has been replaced by 0 since we are _not_ recentering.
# 
# **Note**: We set `ddof=0` so that the large-sample standard deviation estimator is used, 
# $$\hat{\sigma} = \sqrt{n^{-1} \sum_{i=1}^n (X_i - \bar{X})^2}$$

#%%


#%%
# ## LASSO
# 
# `LassoCV` can be used to cross-validate the tuning parameter (`alpha` is scikit-learn is the same as $\lambda$ in the notes). Here we set `fit_intercept` to `False` since the model should not include an intercept.  We then choose the tuning parameter by cross-validation and report the optimal value and the estimated coefficients.

#%%


#%%
# We used transformed `x` and `y` values, and so to get the parameters back to the scale of the original data, we need to multiply by the ratio of the two scales.  The invariance to affine transformations is a standard property of OLS estimators.  Note the model we estimated was
# 
# $$ \frac{Y_i}{\hat{\sigma}_Y} = \sum_{j=1}^k \beta_j \frac{X_{i,j}}{\hat{\sigma}_{X_j}}  + \epsilon _i $$
# 
# so to get back to the original scale we need to multiply the estimated coefficient for regressor $j$ by
# 
# $$ \frac{\hat{\sigma}_Y}{\hat{\sigma}_{X_j}}.$$

#%%


#%%
# ## Ridge Regression
# 
# Ridge regression is virtually identical with the key exception that we need to pass in an arrays of `alpha` values to check.  Here we do this in two passes where the first gets a rough estimate and the second refines this value.  Again `alpha` is the same as $\lambda$ in the notes.

#%%


#%%
# The coefficient need to be rescaled to be comparable to those that we would find by OLS.

#%%


#%%
# The optimal shrinkage is small and the coefficient are similar to those in OLS.  This might not be the case if the sample size was smaller or the number of regressors was larger.

#%%


#%%
# With the rescaled coefficients, we can then compute the actual in-sample predictions with the correct scale.

#%%


#%%
# ## Using scikit-learn to scale
# 
# 
# scikit-learn contains a number of alternative rescaling methods.  The basic one is `StandardScaler` which by default computes
# 
# $$ \tilde{X} = \frac{X-\bar{X}}{\hat{\sigma}_X}.$$
# 
# We can set `with_mean=False` to force $\bar{X}=0$.
# 
# Here we standardize both x and y using `StandardScaler` and show the results are identical. `StandardScaler` is used by first initializing it, then fitting the coefficients to a dataset.  This computes the mean and standard deviation and lets the same scaler be applied to other data later. It also lets the scaling operation be inverted, so that we can transform some standardized value $Z$ to the same scale as the original data
# 
# $$ \ddot{X} = \hat{\sigma}_X Z + \bar{X}.$$
# 
# **Note** `StandardScaler` expects a 2-d input, so we need to transform the `Series` version of y to a `DataFrame`.

#%%


#%%
# To make predictions in the original space of the y values, we first predict using the standardized values, and then we use `inverse_transform` of the `y_scaler` to transform the predictions which are for the standardized y back to the original scale. Aside from the loss of the pandas information, we can see these are the same as the predictions above.

#%%


#%%
# ## Out-of-sample
# 
# The scikit-learn approach makes out-of-sample prediction simple using 3 steps:
# 
# 1. Standardized out-of-sample x values using the `x_scaler`. **Note**: This must be the same scaler used previously.
# 2. Make a prediction using the transformed out-of-sample x values.
# 3. Inverse the transformation of the prediction using `y_scaler`.
# 
# **Note**: We _do not_ rescale the out-of-sample y values.

#%%


#%%
# Predictions from ridge regression are virtually identical. The only caveat in the code is thar Ridge likes 2d arrays, and so `pred` is 2d. This needs to be squeezed to 1d before running through `inverse_transform`.

#%%


#%%
# For good measure we can compare to OLS.  We see that both shrinkage methods have outperformed OLS despite the small differences in coefficients.

#%%


#%%
# It is also possible to directly compute the out-of-sample predictions using the transformed regression coefficients computed previously.  When the coefficients have been transformed, the remainder of the calculation is simple.

#%%


#%%
# We can compare the predictions using the two methods and see they are identical.

#%%

