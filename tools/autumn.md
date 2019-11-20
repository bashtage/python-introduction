# Data: Dataset Construction


# Concatenations
## `pd.concat`

* Concatenation directly extends `Series` and `DataFrames`
  * Essentially _stacks_ multiple pandas objects
* Use `axis=1` for horizontal concatenation (columns)
  * Default is `axis=0`, vertical concatenation (rows)
 
```python
combined = pd.concat([a, b, c], axis=1)
```

* `a`, `b`, and `c` are `DataFrame`s with the same index


# Reproducible Random Numbers
## Compatibility (Legacy)

* `np.random.RandomState` is seedable
* Using the same produces the same set of random numbers

```python
import numpy as np
seed = 2725404939
rs = np.random.RandomState(seed)
print(rs.standard_normal())
rs_alt = np.random.RandomState(seed)
# Identical
print(rs_alt.standard_normal())
```

* Seeds need to be in $[0, 2^{32})$
  * Can also be array of values in same range


# Reproducible Random Numbers
## NumPy v1.17 or later

* New code to generate random values in NumPy 1.17+
* Uses `np.random.Generator` in place of `RandomState`
* Initialize using `np.random.default_rng`

```python
import numpy as np
seed = 161932852906181212798210784490480099595
gen = np.random.default_rng(seed)
print(gen.standard_normal())
alt_gen = np.random.default_rng(seed)
# Identical
print(alt_gen.standard_normal()) 
```

* Can easily use integer seeds of any length


# Reproducible Random Numbers
## Using `scipy.stats`

* **Warning**: `scipy.stats.`_dist_ `.rvs` relies on hidden default `RandomState` instance
  * To make reproducible, you must set the seed of default `RandomState`
 
```python
import numpy as np
from scipy import stats

seed = 2725404939
np.random.seed(seed)
print(stats.chi2(5).rvs(2))
np.random.seed(seed)
# Identical
print(stats.chi2(5).rvs(2))
```

* Alternatively use `get_state` and then `set_state`


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
