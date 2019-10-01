#!/usr/bin/env python
# coding: utf-8

# # Graphics: Line Plots
# 
# This lesson covers:
# 
# * Basic plotting 
# * Subplots 
# * Histograms 
# * Scatter Plots

# Plotting in notebooks requires using a magic command, which starts with
# `%`, to initialize the plotting backend.

# Setup
get_ipython().run_line_magic('matplotlib', 'inline')


# Begin by loading the data in hf.h5. This data set contains high-frequency
# price data for IBM and MSFT on a single day stored as two Series. IBM is
# stored as 'IBM' in the HDF file, and MSFT is stored as 'MSFT.




# ## Problem: Basic Plotting
# 
# 1. Plot the `ibm` series which contains the price of IBM. 
# 2. Add a title and label the axes. 
# 3. Add markers and remove the line. 










# ## Problem: Subplot
# 
# Create a 2 by 1 subplot with the price of IBM in the top subplot and the
# price of MSFT in the bottom subplot. 




# ## Problem: Plot with Dates
# 
# Use `matplotlib` to directly plot `ibm` against its `index`. This is a
# repeat of a previous plot but shows how to use the `plot` command directly. 



