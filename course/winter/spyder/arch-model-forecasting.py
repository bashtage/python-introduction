#!/usr/bin/env python
# coding: utf-8

# %%
# ## ARCH Model Forecasting
#
# **Functions**
#
# `sm.OLS`, `sm.WLS`
#
#
# ### Exercise 77
#
# Use 50% of the sample to estimate your preferred GARCH model for returns to the S&P 500 and the
# EUR/USD rate, and construct forecasts for the remaining period.

# %%


# %%
# ### Exercise 78
#
# Evaluate the accuracy of the forecasts.

# %%


# %%
# We can also use a weighted LS estimator where the variance is the inverse
# of the squared forecast.  The creates the MZ-GLS test.
#

# %%


# %%
# ### Exercise 79
#
# Evaluate the accuracy of forecasts from a 2-year backward moving average variance.

# %%


# %%
# ### Exercise 80
#
# Compare the ARCH-model forecasts to a naive 2-year backward looking moving average using QLIKE.

# %%
