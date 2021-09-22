#!/usr/bin/env python
# coding: utf-8

#%%
# ## ARMA Modeling: Residual Diagnostics
#
# **Functions**
#
# `tsa.SARIMAX`, `sm.stats.diagnostic.acorr_ljungbox`, `SARIMAXResults.test_serial_correlation`,
# `statsmodels.sandbox.stats.diagnostic.acorr_lm`
#
# ### Exercise 69
# Compute the residuals from your preferred model from the previous exercise, as well as a random-walk model.
#
# 1. Plot the residuals
# 2. Is there evidence of autocorrelation in the residuals?
# 3. Compute the Q statistic from both sets of residuals. Is there evidence of serial correlation?
# 4. Compute the LM test for serial correlation. Is there evidence of serial correlation?

#%%
