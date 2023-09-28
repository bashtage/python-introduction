#!/usr/bin/env python
# coding: utf-8

# %%
#
# ## Maximum Likelihood Estimation
#
# **Functions**
#
# `np.log`, `scipy.special.gamma`, `scipy.special.gammaln`, `scipy.stats.norm.cdf`, `scipy.optimize.minimize`,
# `scipy.stats.t`, `np.var`, `np.std`, `scipy.stats.norm.pdf`
#
# ### Exercise 20
#
# Simulate a set of i.i.d. Student's t random variables with degree of freedom
# parameter $\nu=10$. Standardize the residuals so that they have unit variance
# using the fact that $V\left[x \right]=\frac{\nu}{\nu-2}$. Use these to estimate
# the degree of freedom using maximum likelihood. Note that the likelihood of
# a standardized Student's t is
#
# $$f(x;\nu,\mu,\sigma^{2})=\frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)}\,\frac{1}{\sqrt{\pi(\nu-2)}}\,\frac{1}{\sigma}\,\frac{1}{\left(1+\frac{\left(x-\mu\right)^{2}}{\sigma^{2}(\nu-2)}\right)^{\frac{\nu+1}{2}}}$$
#
# where $\Gamma\left(\right)$ is known as the gamma function.

# %%


# %%
# ### Exercise 21
#
# Repeat the previous exercise using daily, weekly and monthly S&P 500 and Hang Seng data.
# Note that it is necessary to remove the mean and standardize by the standard deviation
# error before estimating the degree of freedom. What happens over longer horizons?

# %%


# %%
# ### Exercise 22
#
# Repeat the previous problem by estimating the mean and variance simultaneously with
# the degree of freedom parameter.

# %%


# %%
# ### Exercise 23
#
# Simulate a set of Bernoulli random variables $y_{i}$ where
#
# $$p_{i}=\Phi\left(x_{i}\right)$$
#
# where $X_{i}\sim N\left(0,1\right)$. (Note: $p_{i}$ is the probability of
# success and $\Phi\left(\right)$ is the standard Normal CDF). Use this simulated data to
# estimate the Probit model where $p_{i}=\Phi\left(\alpha_{0}+\alpha_{1}x_{i}\right)$
# using maximum likelihood.

# %%


# %%
# ### Exercise 24
#
# Estimate the asymptotic covariance of the estimated parameters in the previous.
#
# The derivative of the log-likelihood for a single observation is
#
# $$ \frac{\partial \left\{y_i \ln\left(\Phi\left(\alpha_0+\alpha_1 x_i \right)\right) + \left(1-y_i\right) \ln\left(1-\Phi\left(\alpha_0+\alpha_1 x_i \right)\right)\right\}}{\partial \alpha_j} $$
#
# which is
#
# $$ y_i \frac{\phi\left(\alpha_0+\alpha_1 x_i \right)}{\Phi\left(\alpha_0+\alpha_1 x_i \right)} - \left(1-y_i\right)\frac{\phi\left(\alpha_0+\alpha_1 x_i \right)}{1-\Phi\left(\alpha_0+\alpha_1 x_i \right)} $$
#
# for $\alpha_0$ and
#
# $$ y_i x_i \frac{\phi\left(\alpha_0+\alpha_1 x_i \right)}{\Phi\left(\alpha_0+\alpha_1 x_i \right)} - \left(1-y_i\right)x_i\frac{\phi\left(\alpha_0+\alpha_1 x_i \right)}{1-\Phi\left(\alpha_0+\alpha_1 x_i \right)} $$
#
# for $\alpha_1$ where $\Phi(\cdot)$ is the cdf of a standard Normal random variable and
# $\phi(\cdot)$ is the pdf of a standard Normal random variable.
#

# %%
