#!/usr/bin/env python
# coding: utf-8

#%%
# ## Value-at-Risk: Using Filtered Historical Simulation
# 
# **Functions**
# 
# `arch_model`, `ARCHModelResult.std_resid`, `np.percentile`
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
# We can construct the 5-step ahead forecasts by simulating the model forward.
# Note that the first out-of-sample variance is known at time $t$, and so we
# only simulat for `i > 0`. Once we have the simulated $\epsilon$, we then then
# simulate the 5 returns and the total return over 5 days using `sum`. Finally,
# we use `percentile` to find the 5% quantile. 

#%%


#%%
# ### Explanation
# 
# Finally, we shift it by 5 places so that the forecast lines up with the point
# where we will evaluate it.

#%%


#%%
# ### Explanation
# 
# We can plot the 1- and 5-day Value-at-Risks.

#%%


#%%
# ### Explanation
# 
# Finally, we generalize the code above to allow simulation over any `horizon`.
# Thie code is virtually identical to the 5-step forecasts except that it has
# been wrapped in a function.

#%%


#%%
# ### Explanation
# 
# We can use the function to produce the forecasts with a basic loop.

#%%


#%%
# ### Explanation
# 
# We shift to the evaluation point. 

#%%


#%%
# ### Explanation
# 
# Finally we can plot all three Value-at-Risks.

#%%
# #### EUR/USD Value-at-Risk
# 
# We can repeat the VaR calculation for the EUR/USR return using the function.

#%%


#%%
# ### Explanation
# 
# We start by using the function to compute the FHS VaR for the EUR-USD rate for
# all 3 horizons. We plot both VaRs. Finally, we save the VaRs to use in a later
# lesson.
# 

#%%

