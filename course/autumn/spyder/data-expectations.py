#!/usr/bin/env python
# coding: utf-8

#%%
# ## Expectations
# 
# **Functions**
# 
# `np.random.RandomState`, `RandomState.standard_normal`, `RandomState.standard_t`, `RandomState.chi2`,
# `np.exp`, `np.mean`, `np.std`, `scipy.integrate.quadrature`, `scipy.integrate.quad`

#%%
# ### Exercise 10
# 
# Compute $E\left[X\right]$, $E\left[X^{2}\right]$, $V\left[X\right]$ and the kurtosis of $X$ using Monte Carlo integration when $X$ is distributed:
# 
# 1. Standard Normal
# 2. $N\left(0.08,0.2^{2}\right)$
# 3. Students $t_{8}$
# 4. $\chi_{5}^{2}$
# 
# 

#%%


#%%


#%%


#%%


#%%


#%%
# ### Exercise 11 
# 
# 1. Compute $E\left[\exp\left(X\right)\right]$ when $X\sim N\left(0.08,0.2^{2}\right)$.
# 2. Compare this to the analytical result for a Log-Normal random variable.
# 

#%%


#%%


#%%
# ### Exercise 12
# 
# Explore the role of uncertainty in Monte Carlo integration by increasing the number of simulations 300% relative to the base case.
# 

#%%


#%%
# ### Exercise 13
# 
# Compute the expectation in exercise 11 using quadrature.
# 
# **Note**: This requires writing a function which will return $\exp\left(x\right)\times\phi\left(x\right)$ where $\phi\left(x\right)$ is the pdf evaluated at $x$.

#%%


#%%


#%%
# ### Exercise 14 
# 
# **Optional** (Much more challenging)
# 
# Suppose log stock market returns are distributed according to a Students t with 8 degrees of
# freedom, mean 8% and volatility 20%. Utility maximizers hold a portfolio consisting of a
# risk-free asset paying 1% and the stock market. Assume that they are myopic and only care
# about next period wealth, so that 
# 
# $$U\left(W_{t+1}\right)=U\left(\exp\left(r_{p}\right)W_{t}\right)$$
# 
# and that $U\left(W\right)=\frac{W^{1-\gamma}}{1-\gamma}$ is CRRA with risk aversion $\gamma$.
# The portfolio return is $r_{p}=wr_{s}+\left(1-w\right)r_{f}$ where $s$ is for stock market
# and $f$ is for risk-free. A 4th order expansion of this utility around the expected wealth
# next period is
# 
# $$E_{t}\left[U\left(W_{t+1}\right)\right]\approx\phi_{0}+\phi_{1}\mu_{1}^{\prime}+\phi_{2}\mu_{2}^{\prime}+\phi_{3}\mu_{3}^{\prime}+\phi_{4}\mu_{4}^{\prime}$$
# 
# where
# 
# $$\phi_{j}=\left(j!\right)^{-1}U^{\left(j\right)}\left(E_{t}\left[W_{t+1}\right]\right),$$
# 
# $$U^{(j)}=\frac{\partial^{j}U}{\partial W^{j}},$$
# 
# $$\mu_{k}^{\prime}=E_{t}\left[\left(r-\mu\right)_{p}^{k}\right],$$
# 
# and $\mu=E_{t}\left[r_{p}\right]$. Use Monte Carlo integration to examine how the weight in
# the stock market varies as the risk aversion varies from 1.5 to 10. Note that when $\gamma=1$, $U\left(W\right)=\ln\left(W\right)$.
# Use $W_{t}=1$ without loss of generality since the portfolio problem is homogeneous of degree 0 in wealth.

#%%

