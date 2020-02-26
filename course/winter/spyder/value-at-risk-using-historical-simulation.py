#!/usr/bin/env python
# coding: utf-8

#%%
# ## Value-at-Risk: Using Historical Simulation
# 
# **Functions**
# 
# `Series.quantile`, `Series.rolling`

#%%
# ### Exercise 58
# Compute the 1-, 5- and 10-day historical simulation VaR for the S&P 500 and
# the EUR/USD rate.
# 
# **Note**: Start the historical simulation at 25% of the data, and then build the
# additional forecasts using a recursive scheme.

#%%


#%%
# ### Explanation
# 
# We start by loading the indices and transforming each into percentage returns.

#%%


#%%
# ### Explanation
# 
# pandas exposes an interface for `expanding` window statistics which is virtually
# identical to the `rolling` window interface. The key parameter is `min_periods`
# which sets the smallest sample that will be used.  A key feature of `expanding`
# is that the statistic computed using observations $0$, $1$, $\ldots$, $m$ are
# placed in position $m$. In code notation, `stat[m] = func(data[:(m+1)])`.  This
# is important when forecasting since the value in position $m$ is the forecast
# for `m+1`. We could use `shift` to move it forward 1 observation, which aligns the
# forecast with its realization.

#%%


#%%
# ### Explanation
# 
# To implement HS over longer horizons, we first need to compute the $h$-day return.
# We construct the returns using `rolling(h).sum()`. Finally, we can use `expanding`
# on the 5-day returns to compute the expanding set of quantiles. Again, these are
# aligned at the point where the forecast is made, not where it is forecasting.

#%%


#%%
# ### Explanation
# 
# The 10-day VaR is virtually identical, using `rolling` and then `expanding`.

#%%


#%%
# ### Explanation
# 
# We can join the three VaRs into a single DataFrame and then plot them.

#%%


#%%
# ### Explanation
# 
# We can use the same process to automate the process for the EUR/USD rate.
# While it is wasteful to use `rolling(1)` for the 1-step VaR, uniformly
# applying this method simplified the code. Finally, we can plot the series.
# 
# The function `ax.set_yticklabels` allows us to set the string labels
# of the y-ticks, which we get with `ax.get_yticks`.

#%%

