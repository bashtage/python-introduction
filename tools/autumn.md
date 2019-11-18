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

* TODO
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
