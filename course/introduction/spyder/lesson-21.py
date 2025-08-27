#!/usr/bin/env python
# coding: utf-8

# %%
# # Graphics: Line Plots
#
# This lesson covers:
#
# * Basic plotting
# * Subplots
# * Histograms
# * Scatter Plots

# %%
# Plotting in notebooks requires using a magic command, which starts with
# `%`, to initialize the plotting backend.

# %%
# Setup
import matplotlib.pyplot as plt

plt.rc("figure", figsize=(16, 6))  # Improves figure size


# %%
# Begin by loading the data in hf.h5. This data set contains high-frequency
# price data for IBM and MSFT on a single day stored as two Series. IBM is
# stored as "IBM" in the HDF file, and MSFT is stored as "MSFT.

# %%


# %%
# ## Problem: Basic Plotting
#
# 1. Plot the `ibm` series which contains the price of IBM.
# 2. Add a title and label the axes.
# 3. Add markers and remove the line.

# %%


# %%


# %%


# %%
# ## Problem: Subplot
#
# Create a 2 by 1 subplot with the price of IBM in the top subplot and the
# price of MSFT in the bottom subplot.

# %%


# %%
# ## Problem: Plot with Dates
#
# Use `matplotlib` to directly plot `ibm` against its `index`. This is a
# repeat of a previous plot but shows how to use the `plot` command directly.

# %%


# %%
# ## Exercises
#
# ### Exercise: Change seaborn
#
# Produce a line plot of MSFT's price using seaborn's "whitegrid" style.

# %%


# %%
# ### Exercise: HLOC plot
#
# Use the HLOC data to produce a plot of MSFT's 5 minute HLOC
# where the there are no lines, high is demarcated using a green triangle,
# low is demarcated using a red downward pointing triangle, open is demarcated
# using a light grey leftward facing triangle and close is demarcated using
# a right facing triangle.
#
# **Note** Get the axes from the first, plot, and reuse this when plotting
# the other series.

# %%
# Setup: Load data and create values
import pandas as pd

msft = pd.read_hdf("data/hf.h5", "MSFT")
msft_5min = msft.resample("300s")
high = msft_5min.max()
low = msft_5min.min()
open = msft_5min.first()
close = msft_5min.last()


# %%
