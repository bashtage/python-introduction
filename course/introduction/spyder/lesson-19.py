#!/usr/bin/env python
# coding: utf-8

# # Graphics: Other Plots
# 
# This lesson covers:
# 
# * Histograms 
# * Scatter Plots

# Plotting in notebooks requires using a magic command, which starts with `%`,
# to initialize the plotting backend.

# Setup
get_ipython().run_line_magic('matplotlib', 'inline')


# Begin by loading the data in hf.h5. This data set contains high-frequency
# price data for IBM and MSFT on a single day stored as two Series. IBM is
# stored as "IBM" in the HDF file, and MSFT is stored as "MSFT.




# ## Problem: Histogram
# 
# Produce a histogram of MSFT 1-minute returns (Hint: you have to produce
# the 1-minute Microsoft returns first using `resample` and `pct_change`).




# ## Problem: Scatter Plot
# 
# Scatter the 5-minute MSFT returns against the 5-minute IBM returns.
# 
# *Hint*: You will need to create both 5-minute return series, merge them,
# and then plot using the combined DataFrame. 




# ## Problem: Saving plots
# 
# Save the previous plot to PNG and PDF.



