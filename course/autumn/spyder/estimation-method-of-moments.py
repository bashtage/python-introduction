#!/usr/bin/env python
# coding: utf-8

#%%
# ## Method of Moment Estimation
# 
# **Functions**
# 
# `DataFrame.mean`, `DatFrame.sum`, `plt.subplots`, `plt.plot`, `stats.kurtosis`, `stats.skewness`
# 
# ### Exercise 16
# Estimate the mean, variance, skewness and kurtosis of the S&P 500 and Hang Seng using
# the method of moments using monthly data.

#%%


#%%
# ### Exercise 17
# Estimate the asymptotic covariance of the mean and variance of the two series (separately,
# but not the skewness and kurtosis). 

#%%


#%%
# ### Exercise 18
# Estimate the Sharpe ratio of the two series and compute the asymptotic variance of
# the Sharpe ratio. See Chapter 2 of the notes for more on this problem.
# 
# 
# The asymptotic variance is computed as 
# 
# $$ D \Sigma D^\prime$$
# 
# where
# 
# $$ D = [\sigma^{-1}, -1/2 \mu \sigma^{-3} ] $$
# 
# and $\Sigma$ is the asymptotic covariance of the mean and variance. Finally, we
# divide by $n$ the sample size when computing the statistic variance. 

#%%


#%%
# 
# ### Exercise 19
# Plot rolling estimates of the four moments using 120 months of consecutive data using a
# 4 by 1 subplot against the dates.
# 
# The simple approach to this problem uses a loop across 120, 121, ..., $n$ and computes
# the statistics using 120 observations. The figure is then created with a call to `plt.subplots`
# and the series can be directly plotted by calling `ax.plot`.
# 
# The pandas-centric approach uses teh `rolling` method to compute rolling statistics and
# then uses `.plot.line` with `subplots=True` to produce the plot.

#%%

