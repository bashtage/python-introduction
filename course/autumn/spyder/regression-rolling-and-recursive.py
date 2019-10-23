#!/usr/bin/env python
# coding: utf-8

#%%
# ## Rolling and Recursive Regressions
# 
# **Functions**
# 
# `sm.OLS`, `plt.title`, `plt.legend`, `plt.subplots`, `plt.plot`
# 
# ### Exercise 47
# For the same portfolios in the previous exercise, compute rolling $\beta$s
# using 60 consecutive observations.

#%%


#%%


#%%
# ### Exercise 48
# 
# For each of the four $\beta$s, produce a plot containing four series: 
# 
# * A line corresponding to the constant $\beta$ (full sample) 
# * The $\beta$ estimated on the rolling sample 
# * The constant $\beta$ plus $1.96 \times$ the variance of a 60-observation estimate of $\beta$. 
#   The 60-month covariance can be estimated using a full sample VCV and rescaling it by T/60 
#   where T is the length of the full sample used to estimate the VCV. Alternatively, the VCV
#   could be estimated by first estimating the 60-month VCV for each sub-sample and then averaging
#   these.
# * The constant $\beta$ minus $1.96 \times$ the variance of a 60-observation estimate of $\beta$. 

#%%


#%%
# ### Exercise 49
# 
# Do the factor exposures appear constant?

#%%


#%%
# ### Exercise 50
# 
# What happens if only the market is used as a factor (repeat the exercise excluding SMB and HML).

#%%


#%%


#%%

