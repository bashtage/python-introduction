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
 