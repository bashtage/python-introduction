# Data: Dataset Construction


# Concatenations
## `pd.concat`

* Concatentation directly extends `Series` and `DataFrames
* Use `axis=1` for horizontal concatentation (columns)
  * Default is `axis=0`, vertical concatentation (rows)
 
```python
combined = pd.concat([a, b, c], axis=1)
```

* `a`, `b`, and `c` are `DataFrame`s with the same index


# Reproducible Random Numbers
## Compatibility (Legacy)


# Reproducible Random Numbers
## Current Best Practice


# Reproducible Random Numbers
## Using `scipy.stats`

* **Warning**: `scipy.stats.`_dist_`.rvs` does **not** support the modern generator
  * To make reproducible, you must set the state of default NumPy `RanomState`
 
```python
import numpy as np
from scipy import stats

state = np.random.get_state()
print(stats.chi2(5).rvs(2))
np.random.set_state(state)
print(stats.chi2(5).rvs(2))  # Match
```


# Quadrature
## `scipy.integrate`

* Key functions:
  * `quadrature`: Adaptive Gaussian quadrature
  * `romberg`: Romberg integration
  * Others: `newton_cotes`, `fixed_quad`, `dblquad`
* Common signature
  * First input is a function to integrate
    * One input: the integration variable
    * One output: the function value
  * Next two are integration bounds

```python
from scipy.integrate import quadrature
def f(x):
    return x**2
quadrature(f, 0, 1)
```

* Returns integral and accuracy information


