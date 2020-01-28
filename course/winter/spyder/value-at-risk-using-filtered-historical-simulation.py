#!/usr/bin/env python
# coding: utf-8

#%%
# ## Value-at-Risk: Using Filtered Historical Simulation
# 
# **Functions**
# 
# `arch_model`, `ARCHModelResult.std_resid`
# 
# ### Exercise 59
# Use a GARCH(1,1) model to construct filtered historical VaR for the S&P 500 and
# the EUR/USD exchange rate, using 10 years of data.
# 
# **Note**: For simplicity, estimate the model on the full sample, but start the
# historical simulation at 25% of the data, and then build the additional forecasts
# using a recursive scheme.

#%%


#%%
# ### Explanation
# 
# We start out by loading the index data, computing percentage returns
# and then estimating a GARCH(1,1) on the S&P 500 returns.

#%%


#%%
# ### Explanation
# 
# The 1-step FHS 95% VaR requires three inputs: the conditional mean and
# variance and the quantile of the standardized residuals.  The mean is
# constant and so can be determined from the model parameters. The 1-step
# ahead variance can be computed using the `forecast` method. The forecast
# variance is returns in a DataFrame in the column `h.1`. This value is
# origin-aligned so that the value in position $m$ is the forecast for
# period $m+1$.  Finally, we need to quantile of the standardized residuals.
# This is computed on an expanding basis using the same method that was used
# to construct HS VaR in the previous lesson. 
# 
# Finally, these are combined to produce the VaR.  Note that we use
# $-\mu - \sigma q_{0.05}$ since we want the VaR to be positive in most
# situations and $q_{0.05}$ is usually negative.

#%%


#%%
# ### Explanation
# Here we plot the one-step ahead VaR.
# 

#%%


#%%
# ### Explanation
# 
# Multi-step VaR is harder.  We need to simulate returns for $h$ days and then take
# the quantile of the simulated returns. While `arch` can do this for us, it is
# instructive to manually implement the steps. We start with a single day,
# and then wrap that in a loop to compute the 5-day VaR for the entire sample.

#%%


#%%
# ### Explanation

#%%


#%%
# ### Explanation

#%%


#%%
# ### Explanation

#%%


#%%
# ### Explanation

#%%


#%%
# ### Explanation

#%%


#%%
# ### Explanation

#%%


#%%
# ### Explanation

#%%
# ### Exercise 60
# 
# Compare this VaR to the HS VaR in the previous example.

#%%


#%%
# ### Explanation
