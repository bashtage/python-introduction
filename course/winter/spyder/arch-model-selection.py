#!/usr/bin/env python
# coding: utf-8

#%%
# ## ARCH Model Selection
# 
# ### Exercise 53
# 
# Which model is selected for the S&P 500 among the classes:
# a. TARCH
# b. GJR-GARCH
# c. EGARCH

#%%


#%%
# Start with a baseline GARCH(1,1,1) 

#%%


#%%
# #### Discussion
# 
# We can then extend this model with an asymmetry into a GJR-GARCH(1,1,1). 
# The asymmetry term is highly significant and eliminates the symmetric term.

#%%


#%%
# #### Discussion
# 
# We can then expand these to see if more lags are needed.  The
# (1,1,1) specification appears to be adequate.
#  

#%%


#%%


#%%
# #### Discussion
# 
# Next, we can examine how a TARCH performs relative to a GJR.  It produces
# a higher likelihood and so is preferred.

#%%


#%%
# #### Discussion
# 
# We can also examine additional lags in the TARCH. These are
# both insignificant. 

#%%


#%%


#%%
# #### Discussion
# 
# Finally, we can look at an EGARCH model. This model cannot be
# easily constructed using the ``arch_model``. Instead, we need
# to build it from the mean component ``ConstantMean`` and the 
# volatility process ``EGARCH``. 
# 
# This model produces a lower log-likelihood than the TARCH model
# and so we finally select the TARCH.

#%%

