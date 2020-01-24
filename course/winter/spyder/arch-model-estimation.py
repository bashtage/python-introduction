#!/usr/bin/env python
# coding: utf-8

#%%
# ## ARCH Model Estimation
# 
# **Functions**
# 
# `arch.arch_model`

#%%
# ### Exercise 50
# 
# Download 10 years of data for the S&P 500 and the EUR/USD exchange rate from FRED.
# 

#%%


#%%
# #### Discussion
# We can use pandas-datareader to download the data from FRED.  The data is then
# stored to HDF for use later.  The `if` statement checks if the HDF file already
# exists, and if found, skips downloading the data.
#  

#%%
# ### Exercise 51
# 
# Estimate a GARCH(1,1) and a GJR-GARCH(1,1,1) to the returns of both series.
# 
# **Note**: You need to install arch using
# 
# ```bash
# pip install arch
# ```
# 
# which contains ARCH and related models.
# 
# Documentation and examples for the arch package [are available online](https://bashtage.github.io/arch).

#%%


#%%


#%%
# #### Discussion
# The default model is a GARCH(1,1).  The function `arch_model` returns the model, and
# the method `fit` estimates the parameters.  This is the same pattern as in `statsmodels`. 

#%%


#%%
# #### Discussion
# 
# A GJR-GARCH sets the parameter `o` to 1.  I set `p` and `q` for clarity. The
# default values for these two parameters is already 1. 

#%%


#%%


#%%
# ### Exercise 52
# Comment on the asymmetry.
# 
#   * Compare robust and non-robust standard errors.
#   * Plot the fit variance and fit volatility.
#   * Plot the standardized residuals.
# 

#%%


#%%
# #### Discussion
# 
# We can set `disp` to "off" to suppress output.  
# 

#%%


#%%
# #### Discussion
# We can use the `plot` method on the result to plot the annualized volatility.
# The top panel contains the standardized residuals,
# 
# $$ \frac{\left(r_t-\hat{\mu}\right)}{\hat{\sigma}_t}. $$
# 
# The bottom shows the conditional volatility.

#%%


#%%
# #### Discussion
# 
# The result contains the volatility which must be squared to get the conditional
# variance. 
# 
