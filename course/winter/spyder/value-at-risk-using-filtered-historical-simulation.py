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

