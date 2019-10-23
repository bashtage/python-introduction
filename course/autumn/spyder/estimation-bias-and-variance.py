#!/usr/bin/env python
# coding: utf-8

#%%
# ## Bias and Verification of Standard Errors
# 
# Methods/Functions
# 
# `mean`, `var`, `RandomState`, `RandomState.chisquare`, `array`, `DataFrame.plot.kde`, `stats.norm.ppf`

#%%
# ### Exercise 24.
# Simulate a set of i.i.d. $\chi_{5}^{2}$ random variables and use the method of moments
# to estimate the mean and variance.

#%%


#%%
# ### Exercise 25.
# Compute the asymptotic variance of the method of moment estimator.

#%%


#%%
# ### Exercise 26.
# Repeat Exercises 24 and 25 a total of 1000 times.
# Examine the finite sample bias of these estimators relative to the true values.

#%%


#%%
# ### Exercise 27.
# Repeat Exercises 24 and 25 a total of 1000 times.
# Compare the covariance of the estimated means and variance (1000 of each) to the asymptotic covariance of the parameters (use the average of the 1000 estimated variance-covariances). Are these close? How does the sample size affect this?

#%%


#%%
# ### Exercise 28.
# In the previous problem, for each parameter, form a standardized parameter estimate as
# 
# $$z_{i}=\frac{\sqrt{n}\left(\hat{\theta}_{i}-\theta_{i,0}\right)}{\sqrt{\hat{\Sigma}_{ii}}}$$ 
# 
# where
# 
# $$\sqrt{n}\left(\hat{\theta}-\theta_{0}\right)\stackrel{d}{\rightarrow} N\left(0,\Sigma\right)$$
# 
# so that $\hat{\Sigma}$ is the estimated asymptotic covariance. What percent of these $z_{i}$
# are larger in absolute value than 10%, 5% and 1% 2-sided critical values from a normal?

#%%


#%%
# ### Exercise 29.
# Produce a density plot of the $z_{i}$ standardized parameters and compare to a standard normal.

#%%


#%%
# ### Exercise 30.
# Repeat the same exercise for the Bernoulli problem from the previous question.

#%%


#%%


#%%

