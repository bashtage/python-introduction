# Introduction


# Goals

* Familiarity with the PyData stack
  * NumPy
  * pandas
  * SciPy
  * matplotlib
  * statsmodels
* Sufficient knowledge to use Python for data analysis
  * Data analysis
  * Simulation
  * Visualization


# Non-goals

* Mastery of the NumPy/pandas API
* Writing complete applications
* Modeling data
  * Follow-up course
* Expertise in machine learning
* Writing high-performance code
  * Focus on _good_ practice



# Installation


# Installation
## Overview

* Three core components
* Anaconda
  * Python distribution
  * High performance mathematical libraries
* Development environments
  * Visual Studio Code (VS Code)
  * Pycharm Professional
  * Spyder is included in Anaconda


# Installation
## Summary

* Three core components
* Anaconda
* Visual Studio Code (VS Code)
  * Require Python extension
* Pycharm Professional
  * Might need to set the Project Interpreter on OSX and Linux



# Lesson 1: Spyder


# Spyder
## Overview

* Native Python development environment
* Included in Anaconda
* Most friendly for beginners
* **No** native support for Jupyter notebooks


# Converting notebooks to Python
## `nbconvert`

* Jupyter nbconvert can convert a notebook to many format
```bash
jupyter nbconvert --to python notebook.ipynb
```
* Requires jupyter_contrib_nbextensions
  * Install using `pip` and the Anaconda prompt
```bash
pip install jupyter_contrib_nbextensions
```


# Spyder
## Summary

* Pros:
  * Free
  * Included in Anaconda
  * Dedicated Python environment
  * Beginner friendly
  * Cell mode
* Cons:
  * No integrated support for Jupyter Notebooks



# Lesson 1: PyCharm Professional


# PyCharm Professional
## Overview

* Commercial Development Environment specialized for Python
* First class support for both Jupyter Notebooks and Cell Mode


# PyCharm Professional
## Summary

* Pros:
  * Feature Rich DE
  * First-class support for Jupyter Notebooks
  * First-class support for cell model (Magic Python)
  * Supports complete spectrum of user needs from stand alone scripts to complete applications
  * Free for most students
    * Deep discount for other academic users
    * **Note**: The free Community Edition is missing required features
* Cons:
  * Resource Heavy
  * Complexity can be intimidating



# Lesson 1: Visual Studio Code


# VS Code
## Overview

* Free, modern text editor
* Supports extensions to add features
  * First-class Python provided by Microsoft
  * AI assistant using Intellicode
* Native supports for Jupyter notebooks
* Support execution of Magic Python files (cell mode)


# VS Code
## Summary

* First-class support for Python provided by Microsoft
* Other extensions add useful features
  * Intellicode: AI assistant
  * Code Spell Checker: Spell checking
* Native support for Jupyter notebooks
  * Requires up-to-date Python extension
* Supports Magic Python cells
  * Cells demarcated with `#%%`



# Lesson 2


# Python Types
## Overview

* Numeric: `float` and `int`
  * Key difference: integers are exact
* String
* List
  * Hold other objects
  * Access by position
  * Closely related to tuples
* Dictionary
  * Hold other objects
  * Access by key


# Numeric Types

* Floating point (`float`)
  * Entered by including a dot
    * `1.2`, `1.0`, `1.`
  * Use an approximation
* Integer (`int`)
  * A number without a dot
    * 1, 1000000000
* If any term is a float, then mathematical operation is a float
  * `2 * 2` produces `4`
  * `2 * 2.0` produces `4.0`
  * `2.0 * 2.0` produces `4.0`


# Strings (`str`)

* Entered using either `"`_string_`"` or `"`_string_`"`
  * Quotation mark must match
* Join strings with `+`
  * `"apple" + "banana"` produces `"applebanana"`
* Repeat string with `*`
  * `"-" * 80` produces `"-----...-----"`
* F-strings allow mixing strings and code
  * Variables in curly braces `{}` are replaced with string versions
  * Equivalent strings
    * f"This is a {number}"
    * "This is a " + str(number)


# Lists (`list`)

* Container for other objects
  * Numbers, strings, lists, etc.
  * Heterogeneous
* Initialized using `[]` syntax
  * `lst = ["a", 1, 1.0, ["b", 2, "2.0"]]`
* Lists are 0-indexed
  * `lst[0]` is the first element
* List of list is important in numerical Python
  * Represents a 2-dimensional array or matrix
  * Each inner list is a row
```python
row1 = [1, 3, 5]
row2 = [2, 4, 6]
matrix = [row1, row2]
direct = [[1, 3, 5], [2, 4, 6]]
```


# List Access

* Access by position
  * `lst[7]`
  * 0-indexed
    * 0 is first element, 1 is second, etc.
* Subset using _slice_
  * `lst[3:9]`
* Add new elements with `.append` method
  * `lst.append("one")`
* Other useful methods
  * `remove` to remove elements
    * `lst.remove(1)`
  * `extend` to extend one list with the contents of another
    * `lst.extend(["c", 3, 3.0])`


# Tuples (`tuple`)

* Tuples (`tuple`) are a close cousin of `list`
* **Key difference**: Cannot be changed once created (_immutable_)
* Created using `(item1, item2, ...)`
```python
tpl = (1, )
tpl = ("a", 1, 1.0, ("b", 2, "2.0"))
```
* Convert to list using `list(tpl)`
* Convert from list using `tuple(lst)`
* Primarily encountered as output of other functions
* Item access is identical to `list`


# Slices
## Subset selection

* Slices are widely used in numerical python
  * Lists
  * NumPy arrays
  * pandas `DataFrames` and `Series`
* Basic syntax
  * `lst[start:stop]`
  * Selects all elements `lst[i]` where `start <= i < stop`
    * `i = start`, `start+1`, `start+2`, ..., `stop-1`
* Common use
  * `lst[:stop]` is the same as `lst[0:stop]`
  * `lst[start:]` is the same as `lst[start:len(lst)]`
    * `len(lst)` is the number of elements in the list


# Dictionaries (`dict`)

* Container for other objects
* Always stored as a key-value pair
* Keys are any _hashable_ object in Python
  * Focus here on strings
* Initialized using `{}`
```python
d = {}
d = {key : value}
d = {key1 : value1, key2: value2, ...}
```
* Add or change elements using `d[key] = value`
  * Element added is `key` not in `d`, otherwise replaced
* Delete elements using `del d[key]`
* Access by key `value = d[key]`


# Python Types
## Summary

* Focus on a small number of native Python types:
  * Numeric: `float` and `int`
  * Strings: `str`
  * Lists: `list`
    * Tuples: `tuple`, list-like but cannot be changed once created
  * Dictionary: `dict`
* Floats, integers and strings are basic data types
* Lists and dictionaries are used to hold other objects



# Lesson 3


# Importing Modules
## Overview

* Python 3.7 provides 64 built-in functions and types
* Core features extended by importing modules
* Standard library modules
  * `math`, `statistics`, `io`
* Key modules for data science and econometrics
  * NumPy, pandas, SciPy, matplotlib, statsmodels


# The `import` statement

* Basic use
```python
import module
```
* Using short names
```python
import module as mod
```
* Importing specific functions or types
```python
from module import func, type
```


# The PyData Ecosystem
* NumPy
  * Basic array and key functions
```python
import numpy as np
```
* pandas
  * User-friendly container for data
```python
import pandas as pd
```
* SciPy
  * Optimization and integration &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  * Manipulating random variables
```python
import scipy as sp
import scipy.stats as stats
```


# The PyData Ecosystem
* matplotlib's PyPlot module
  * Plotting and data visualization
```python
import matplotlib.pyplot as plt
```
  * See `seaborn`
* statsmodels
  * Key statistical model (OLS, ARMA)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```python
import statsmodels.api as sm
import statsmodels.tsa.api
```


# Importing Modules
## Summary

* Modules are added to Python using `import`
* Standard syntax `import` _module_ `as` _canonical_
* Five key modules with canonical names
  * NumPy (`np`)
  * pandas (`pd`)
  * SciPy's Stats module (`stats`)
  * matplotlib's PyPlot (`plt`)
  * statsmodels (`sm` and `tsa`)



# Lesson 4


# `Series` and `DataFrames`
## Overview

* pandas provides two essential containers
  * `Series`: 1-d homogeneous array
  * `DataFrame`: 2-d heterogeneous array
* A `Series` is 1 column from a `DataFrame`
* Both support `index`
  * Defaults to integers: 0, 1, 2, ...
  * Can assign meaningful data: date, company name, ...
* DataFrame supports named columns


# pandas `Series`
## Homogeneous 1-d arrays

* Each column of a `DataFrame` is a `Series`
* Constructed using
```python
s = pd.Series([1,2,3])
```
* Key Optional arguments
  * `index` is the index for the `Series`
  * `name` is same as the column name in a `DataFrame` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```python
idx = ["a","b","c"]
s = pd.Series([1,2,3], index=idx, name="data")
```


# pandas `DataFrame`
## Heterogeneous 2-d arrays

* Each column is a `Series`
* Data types can vary by column
  * Allows mix of integer, floating and string data
* Directly initialized using a list of lists
```python
data = [[1, 2, 3], [4, 5, 6]]
df = pd.DataFrame(data)
```
* Can be created from `Series` or by merging `DataFrames`


# pandas `DataFrame`
## Extended options

* Key optional parameters
  * `columns` takes a list of column names
  * `index` is the index for the `DataFrame`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```python
data = [[1, 2, 3], [4, 5, 6]]
cols = ['A','B','C']
idx = ['x', 'y', 'z']
df = pd.DataFrame(data, columns=cols, index=idx)
```
  * Both can be assigned after initialization
```python
df = pd.DataFrame(data)
df.columns = cols
df.index = index
```


# `Series` and `DataFrames`
## Summary

* A `Series` is a 1-d homogeneous array
* A `DataFrame` is a 2-d heterogeneous array
  * A `Series` is 1 column from a `DataFrame`
* The `index` contains a set of keys corresponding to rows
* `DataFrame` supports keys for columns as well (`columns`)
  * `Series` supports `name` since always 1 column



# Lesson 5


# `DataFrames` from `Series`
## Overview

* Two standard ways to build `DataFrames`
  * Treat each `Series` as a row
```python
df = pd.DataFrame([s1, s2, s3])
```
  * Use a dictionary containing columns &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```python
df = pd.DataFrame({'A': a, 'B': b, 'C': c})
```
    * Keys are column names
* Advanced methods
  * `pd.concat` concatenates `DataFrames`
  * `DataFrame.merge` and `DataFrame.join` are SQL-like


# Creating `DataFrame`s
## Building from  multiple `Series`

* From a list of `Series`
```python
df = pd.DataFrame([s1, s2])
```
  * Each `Series` represents row
  * `Series` `name` becomes index
  * `Series` `index` become columns
    * Component `Series` should have identical `index`
  * Use `.T` to transpose a `DataFrame`


# Creating `DataFrame`s
## Building from  multiple `Series`

* Using a dictionary &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```python
df = pd.DataFrame({'a': s1, 'b': s2})
```
  * Keys are column names
  * Component `Series` should have identical `index`


# `DataFrames` from `Series`
## Summary

* Build `DataFrame` from `Series`
  * `Series` as rows using a list
  * `Series` as columns using a dictionary



# Lesson 6


# Functions and Methods
## Overview

* Functions are used to transform inputs
* Methods are functions attached to an object
  * Method is a function that always take its object as the first input
  * The object is hidden in the method call
```python
a = np.array([1, 2, 3])
a.mean()
np.mean(a)
```
* Both use positional and keyword arguments
* May return one or more outputs
  * Multiple outputs are tuples
  * Directly unpack by matching the number of output


# Calling Functions
* Positional arguments
```python
func(a)
func(a, b)
```
* Keyword arguments &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```python
func(data=a)
func(data=a, index=b)
```
* Mixed
```python
func(a, index=b)
```


# Calling methods on objects

* Python objects expose methods
* Methods operate on the object
* Important examples
  * NumPy arrays
  * pandas `DataFrames` and `Series` all
* Called using _object`.`method_ syntax
```python
a = np.array([1, 2, 3])
a.mean()
```
* Methods can take additional inputs
```python
a.reshape((3, 1))
```


# Multiple Outputs
* Multiple outputs are returned as a tuple
```python
multi_output = func(x, y)
first = multi_output[0]
second = multi_output[1]
```
  * Use positional indexing to unpack
* Can directly unpack multiple returned values
```python
first, second = func(x, y)
```
  * **Warning**: Number of outputs must _exactly_ match the count returned


# Getting Help

* Use `?` to get help in Jupyter notebooks
```python
import pandas as pd
pd.read_csv?
```
  * Does **not** work in VS Code (October 2019)
* Use the `help` built-in

```python
help(pd.read_csv)
```
```python
df = pd.DataFrame([[1],[2]])
help(df.to_csv)
```
* Formatted web-based help easy to find using Google


# Help in Jupyter Server


# Help in PyCharm


# Function Signatures
## Required and Optional Arguments

* Python function can have required or optional arguments
* Function signature indicates type
  * `=` used in optional parameters
  * Value to right of `=` is the default
* Signature for `np.linspace`
```python
linspace(start, stop, num=50, endpoint=True,
           retstep=False, dtype=None, axis=0)
```
  * `start` and `stop` are required
  * 5 other inputs are optional


# Functions and Methods
## Summary

* Functions and methods are widely used
  * Basic statistics
  * Estimation of model parameters (later)
  * Plotting data
* Methods are functions attached to objects
  * Methods operate on the object
  * May take additional inputs
* Parameters either positional or use parameter name
```python
f(1, option="yes")
```
* Help available using `?`, `help` or the web



# Lesson 7


# Custom Functions
## Overview

* Custom functions simplify repetitive code
* Required in some applications
  * Function optimization
  * Numerical integration
* Begin with keyword `def`
* End when indentation level return to previous level
* **Important**: Python is whitespace sensitive


# Custom Functions
## Basic structure
```python
def func(x, y=1):
    function body
    return value
```
  * `def`
  * Function Name (`func`)
  * Arguments surrounded by parentheses `(x)`
    * Support for positional and keyword arguments
    * Keyword argument have default values
  * Colon
  * Function code uses consistent indentation
  * Returned value preceded by `return`


# Custom Functions
## Summary

* Function begin with `def`
* Returned value uses `return`
* Function code is indented
  * **Important**: Python is whitespace sensitive
  * Use 4 spaces to indent
    * Do not use tab character to indent
    * Configure editor to convert tab to 4 spaces



# Lesson 8


# Using DataFrames
## Overview

* `pct_change` creates returns
  * Always creates at least 1 missing value
  * Use `dropna` to remove
* pandas math depends on index and column
  * Does not follow linear algebra rules
  * Exception is matrix multiplication
* Items missing from index or columns produce missing values
* Non-unique index or columns produces duplicates
* Mixing with NumPy falls back to NumPy rules


# Math on pandas types
## Label matching

* Items matched using index or columns
* Missing matches produce missing values
* Repeated indices or column names produce multiplicity of results
  * Care need if not unique


# Specific Cases

* `Series` - `Series`
  * Match on index only, name ignored
* `Series` - `DataFrame`
  * Match `Series` index to `DataFrame` column
  * All values in column use same value from `Series`
* `DataFrame` - `DataFrame`
  * Match on `index` and `columns`
* Exception is `@` (`dot` method)
  * Must confirm using rules of linear algebra


# Math with NumPy arrays

* NumPy rules apply when mixing pandas and numpy
* NumPy rules match linear algebra
* Shape determines if conformable
* Simplest rule: **match dimensions**
* NumPy supports _broadcasting_
  * Allows smaller dimension arrays to be resized
  * Specific circumstances
  * Efficient but complex


# Using DataFrames
## Summary

* Use `pct_change` to create returns
* pandas math matches on index and column
* Care is needed if index/columns is not unique
* Mixing with NumPy uses linear algebra rules
  * Match `DataFrame`/`Series` shape with array



# Lesson 9


# Common DataFrame methods
## Overview

* pandas is batteries included
* Many built-in functions for common tasks
  * Moments
  * Quantiles and Extremes
  * Covariance and Correlation
  * Common `DataFrame` and `Series` specific
* Most operate column-by-column


# Key methods
## Univariate Moments

* Standard behavior
  * Operate column-by-column in a `DataFrame`
  * Return a `Series`
  * Column names are index of `Series` returned
* `mean`: Mean
* `var`: Variance
* `std`: Standard Deviation
* `skew`: Skewness
* `kurt`: Excess kurtosis (standard definition - 3)
* `sum`: Sum


# Key methods
## Quantiles and Extremes

* `median`: Median
* `max`: Maximum
* `min`: Minimum
* `quantile(q)`: User-specified quantile(s), `q` required
  * `quantile` returns a `DataFrame` if `q` is list input
```python
df.quantile([0.25, 0.75])
```
  * `index` matches `q`
  * `columns` match `df.columns`


# Key methods
## Covariance and correlation

* `cov`: Covariance
* `corr`: Correlation
  * Return a diagonally symmetric `DataFrame`
  * Columns and index match


# Key methods
## Mathematics

* Cumulative Statistics
  * `cummax`: Cumulative max
  * `cummin`: Cumulative min
  * `cumprod`: Cumulative product
  * `cumsum`: Cumulative sum
    * Output has same shape as input
* `abs`: Absolute value (element-by-element)
  * Output has same shape as input
* Linear-algebra product
  * `dot`
    * $ x' x\Rightarrow $ `x.T.dot(x)`
    * Output shape depends on inputs


# Key methods
## `DataFrame` specific
* Content information
  * `count`: Number of non-missing values
  * `describe`: Basic summary statistics
* Display
  * `head`: Show first 5 rows
  * `tail`: Show last 5 rows
* Sorting
  * `sort_index`: Sort by index values
  * `sort_values(columns)`: Sort by values of one or more columns
* Size information
  * `ndim`: Number of dimensional (1 or 2)
  * `shape`: Shape of data (`ndim` element tuple)


# Key methods
## Other
* `transpose` (shortcut `.T`)
  * Swap columns and row
* `dropna`: Remove missing
  * Input `how` determines behavior
  * Input `axis` selects to drop rows or columns
* Logical Aggregation
  * `all`: Check if all elements true
  * `any`: Check if any element is true
* Transformation
  * `diff`: Arithmetic change
  * `pct_change`: Percentage change
  * `shift(n)`: Shift values forward or backward


# Common DataFrame methods
## Summary

* pandas includes function for common statistics
  * Moments
  * Quantiles and Extremes
  * Covariance and Correlation
* Many pandas-specific functions
  * `DataFrame`/`Series` information
  * Sorting
  * Transformation
* Most functions operate column-by-column
* Familiarity with the pandas API simplifies coding



# Lesson 10


# Selection in `DataFrames`
## Overview

* Three ways to select using index values or column names
  * `df.loc[`_rows_ `,`_cols_ `]`
  * Dictionary-like syntax
    * Selects columns in a `DataFrame`
    * Selects index in a `Series`
  * `df.`_variable_
    * _variable_ must be a valid Python name
    * Name cannot conflict with a `Series`/`DataFrame` method (`mean`)
* Selection _may_ reduce dimension and change type
* Special features for selecting dates
  * Day, Month, Year
  * Continuous range of dates


# `DataFrame.loc`
## Selection by index and column

* `.loc[`_rows_ `,`_cols_ `]`
  * _rows_ contains element(s) from `index`
  * _cols_ contains element(s) from `columns`
* A single value or a list of values
```python
df.loc["row", ["col1", "col2"]]
```
* Use `:` to select all elements in either
  * Columns are optional if selecting all elements
```python
df.loc[:, ["col1", "col2"]]
df.loc["row", :]
df.loc["row"]
```


# Dictionary-like selection
## Selection by index or column

* `DataFrame`s support dictionary-like syntax
* Selection of columns

```python
df["col"]
df.loc[:, "col"]
```
* List of column names to select multiple

```python
df[["col1", "col2"]]
df.loc[:, ["col1", "col2"]]
```
* `Series` selects using the index

```python
series["row"]
series[["row1", "row2"]]
```


# Single-value Selection
## Dimension reduction

* Single-value selection reduces dimension
* Selection in a `DataFrame` produces a `Series` or a scalar
  * `Series` if selecting in one dimension
  * Scalar if selecting in both

```python
series = df["col"]
series = df.loc["row"]
scalar = df.loc["row", "col"]
```
* Selection in a `Series` produces a scalar value

```python
scalar = series["row"]
scalar = series.loc["row"]
```


# Multiple Selection
## Dimension preservation

* List selection preserves dimension
  * Trivial slice `:` also preserves dimension

```python
new_df = df[["col1", "col2"]]
new_df = df.loc[["row1", "row2"]]
new_df = df.loc[:, ["col1", "col2"]]
```

* Mixed list/single-value reduces dimension

```python
series = df.loc[["row1", "row2"], "col"]
```

* Single-item list preserves dimension

```python
new_df = df.loc[:, ["col"]]
```


# Date Selection
## Special features of `DateTimeIndex`

* Selection by day, month or year using `.loc`
```python
df.loc['1999-12-31']
df.loc['1999-12']
df.loc['1999']
```
* Selection by date-like slice
```python
df.loc['1999-12-31':'2000-12-31']
```
  * **Caveat**: Slice selection is _inclusive_ of the stop value
  * Different behavior from integer slicing, which is exclusive


# Selection in `DataFrames`
## Summary

* Consistently using `.loc` is simplest
* Dictionary syntax depends on type
  * `columns` in a `DataFrame`
  * `index` in a `Series`
* Single-value selection reduces dimension
  * `DataFrame` becomes `Series` or scalar
  * `Series` becomes scalar
* Special features with `DateTimeIndex`
  * String selection of dates
    * Day, Month, Year
    * Range of dates
      * **Caveat**: End point is included



# Lesson 11


# Accessing Elements in Arrays
## Overview

* NumPy `array`s support selection using
  * Scalar integers
  * Slices
  * Lists/arrays of integers
* Selection uses `[]` like a `list`
* Selection can be simultaneously applied to all dimensions
  * Different from `list`

```python
a = np.array([[1,2,3],[4,5,6]])
a[0, :2]
```


# Scalar Selection
## Dimension reduction

* Scalar selection reduces dimension
* Selection dimension is original dimension minus number of scalar selectors
```python
a = np.array([[1,2,3],[4,5,6]])
a[0]  # 1-dim
a[0, 1]  # scalar (0-dim)
```
* Use list to preserve dimension
```python
a[[0]]  # 2-dim, 1 by 3
```


# Slice Selection
## Dimension preserving

* NumPy `arrays` support slicing
* Can use as many slices as the dimension

```python
a = np.array([[1,2,3],[4,5,6]])
a[:1]
a[:, :2]
```
* Trivial slice `:` selects all elements in a dimension
  * Trailing `:`  can be omitted

```python
a[:1]
a[:1, :]
```
* Slicing preserved array dimension


# List Selection
## Dimension preserving

* Individual elements can be selected using ` list` of integers`

```python
a = np.array([[1,2,3],[4,5,6]])
a[:, [0, 2]]
```
* Can only safely use 1 list
  * Safe to mix with scalar or slice selection
* Should use `ix_` to select blocks using lists

```python
a = np.array([[1,2,3],[4,5,6]])
a[np.ix_([0, 1], [0, 2])]  # wrong
a[[0, 1], [0, 2]]  # wrong
```
* `ix_` transforms `list`s into correctly shaped `array`s


# The Trivial Slice
## Using `:`

* Trivial slice `:` selects all elements
* Always selects from 0 to length of a dimension
* `x[:]` is equivalent to `x[0:x.shape[0]]`
* `x[0, :]` is equivalent to `x[:, 0:x.shape[1]]`
* Required when selecting all elements in leading dimensions

```python
x[:, [0, 3]]
```

* Optional in trailing dimensions

```python
x[[0, 3]]
x[[0, 3], :]
```


# Advanced Slicing

* `start:stop:step`
  * `start`, `start+step`, `start+2*step`, `...`
  * Ends when `start + m*step` $\geq$ `stop`
  * `stop` never included
* `-n:`
  * Select the final `n` elements
  * Tail selection
* `-n:-m`
  * Select starting `n` from the end, stop `m` from the end
  * `m` $<$ `n`  
* `::-1`
  * Reverses the order


# Accessing Elements in Arrays
## Summary

* Three methods to select elements
  * Scalar
  * Slice
  * Lists of integers
* Can mix the difference selectors
  * Should only use 1 list unless using `np.ix_`



# Lesson 12


# Numeric Indexing of DataFrames
## Overview

* Numeric indexing complements label indexing
* Uses `.iloc` in place of `.loc`
* Identical to indexing of Numpy Arrays
  * One exception: multiple list selection
  * Always selects blocks
  * As-if `np.ix_` is always used


# `DataFrame.iloc`
## Numeric indexing

* `df.iloc[` _args_ `]` uses numeric position instead of index
  * For example, when computing statistics over a fixed-window

```python
df.iloc[0:60]
df.iloc[1:61]
```

* Support rows only, or rows and columns

```python
df.iloc[0:60]
df.iloc[0:60, 2:4]
```

* Can pass slice, list of integers or scalar integer
  * **Note**: Scalar integer reduces dimension


# `DataFrame.iloc`
## Relationship to `loc`
* Identical `loc` if
  * `index` is 0, 1, ..., `df.shape[0]-1`
  * `columns` is 0, 1, ..., `df.shape[1]-1`
* Equivalent expressions

```python
df.iloc[0:60]
df.loc[df.index[0:60]]
df.iloc[0:60, 2:4]
df.loc[df.index[0:60], df.columns[2:4]]
```
* Saves looking up in index/columns &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


# `DataFrame.iloc`
## Differences with NumPy

* Different from NumPy when using 2 lists
  * Always selects block
  * No need to use `np.ix_`

```python
rows = [0, 2, 5]
cols = [1, 3, 9]
df.iloc[rows, cols]
a[np.ix_(rows, cols)]
```


# Numeric Indexing of DataFrames
## Summary

* Numeric indexing supports
  * Scalars
  * Lists of integers
  * Slices
* Replaces `.loc` with `.iloc`
* Similar to  NumPy array selection
  * Key difference: selection using 2 lists



# Lesson 13


# `for` Loops
## Overview

* Loops simplify repetitive tasks
* Python supports two types of loops
  * `for`
  * `while`
* Focus on simpler `for` loops
  * Two structures are equivalent
* **Whitespace** sensitive
  * Indentation demarcates loop block


# Basic `for` loop
## Core components
```python
for i in range(10):
    print(i)
```
* `for`:  Required keyword
* `i`: value that changes in iterations
* `in`: Required keyword
* `range`: An iterable that generates an integer sequence
  * Alternatives:
    * `list`: Values in the `list`
    * `DataFrame`: Column names (`dict`-like)
    * `Series`: Values in `Series` (`list`-like)
    * NumPy array: First axis
* colon (`:`) required to end declaration


# `for` loop body
## Importance of whitespace
* Loop body **must** be consistently indented
  * **Important**: Python is whitespace sensitive
  * Use 4 spaces
  * **Do not** use tabs, unless tabs converted to spaces
    * Standard features of most Python-focused editors
* body ends when code is dedented (unindented, outdented)

```python
for i in range(10):
    loop_body = 3
    print("Still in body")

not_in_body = "All done"
```


# `range`
## Integer sequence generation

```python
range(stop)
range(start, stop)
```

* `start`: First index
* `stop`: End of range (**not included** in sequence)
```python
 start, start+1, ..., stop-1
```
* `range(stop)` is shorthand for `range(0, stop)`
* Three input variant: `range(start, stop, step)`
  * `step`: Step between values if not 1
  * Usually encountered in decreasing sequences

```python
range(10, 0, -1)  # 10, 9, 8, ..., 1
```


# Nested loops

* Nested using indentation

```python
for i in range(10):
    outer_loop = 1.0
    for j in range(7):
        inner_loop = "!"
        print(f"Still in inner: {j}")
    print(f"Back in outer now: {i}")

print("All done now")
```
* Not recommended to use more than 3 nested loops
  * Use a _function_ if you need more


# `for` Loops
## Summary

* `for` loops iterate across iterable objects
  * `range`: Sequence generator
  * `list`, `dict`, `DataFrame`, `Series`, Numpy array
* **Whitespace** sensitive: Use consistent indentation
* Nesting uses different levels of indentation



# Lesson 14


# Comparison and Logical Operators
## Overview

* 6 comparison operators
  * `<`, `<=`, `==`, `!=`, `>=`, `>`
  * Scalar or vector
* 3 logical operators
  * `and`, `or`, `not`
  * Scalar only
* Operators produce `bool`: `True` or `False`


# Operators

* Comparison operators
  * `<`: Less than
  * `<=`: Less than or equal
  * `==`: Equal
  * `>=`: Greater than or equal
  * `>`: Greater than
  * `!=`: Unequal
* Scalar logical operators
  * `and`: `True` if both are `True`
  * `or`: `True` if either is `True`
  * `not`: `True` if input is `False`
* Logical operators are **scalar** only


# Best Practices

* Good to use parentheses in complex expressions

```python
x > 0 and y < 10
(x > 0) and (y < 10)
not ((x <= 0) or (y >= 10))
```


# Comparison and Logical Operators
## Summary

* 6 comparison operators
* `bool` type
  * `True` and `False`
* 3 logical operators
* Best practice uses parentheses to separate comparison from logical operators  



# Lesson 15


# Boolean Arrays
## Overview

* Created when a NumPy array, `DataFrame` or `Series`  compared using a logical operators
* Always contains `True` or `False`
  * `True` is 1, `False` is 0
* Combining boolean arrays uses `&`, `|` or `~`
  * Equivalent ot `locigal_and`, `logical_or` and `logical_not` functions
  * `and`, `or` and `not` are scalar only
* Uses
  * Selection of elements
  * Summarizing contents
  * Interaction variables


# Array logical operators
```python
c = a & b
c = np.logical_and(a, b)
```
* Elementwise _and_: `c[i]` `True` if `a[i]` and `b[i]` are `True`
```python
c =a | b
c = np.logical_or(a, b)
```
* Elementwise _or_: `c[i]` `True` if `a[i]` or `b[i]` are `True`
```python
c = ~a
c = np.logical_not(a)
```
* Elementwise _not_: `c[i]` `True` if `a[i]` is False


# `any` and `all`
## Logical aggregation

* Common to use `any` or `all` on arrays
* `any` returns `True` is any value is `True`
* `all` returns `True` is all values are `True`
* Reduce vectors to scalars
* Key difference in `DataFrame` methods and NumPy functions
  * `df.any` and `df.all` operator column-by-column
  * `np.any` and `np.all` default to entire array
    * Use `np.any(axis=0)` for column-by-column
* Using `axis=1` operates row-by-row


# Numerical Conversion

* Boolean values are 0/1
* Mathematical operations cast Booleans to integers
  * `sum` counts boolean arrays
  * `mean` computes frequency
  * Multiplication (`*`) produces interactions

```python
x = np.array([-3, 3, 2, -2, -1, 1, 0])
x_neg = x * (x < 0)
```


# Boolean Arrays
## Summary

* Boolean arrays are created using `<`, `<=`, `==`, `>=`, `>`
* Arrays of `True` and `False`
  * `True` is 1 in math ops
* Must use `&`, `|` and `~`
  * Function equivalents: `logical_and`, `logical_or`, `logical_not`
  * `and`, `or` and `not` produce errors
* Boolean selection is identical to integer selection using a list
  * `where(bool_arr)` returns the indices selected
* Use `loc` in pandas to perform logical selection
* In Numpy must use `ix_` with boolean selection in multiple dimensions



# Lesson 16


# Boolean Selection
## Overview

* Boolean arrays can be used to select
  * `True` includes
  * `False` excludes
* Use `.loc` in pandas
* NumPy selection behaves like list of integers
  * Use `np.ix_` when selecting 2 or more axes


# Selection using `.loc`
## `DataFrame` and `Series`

* Logical selection must use `loc`
* Equivalent
```python
sel = (df > 0).any(axis=1)
df.loc[sel]
df.loc[df.index[sel]]
```
* Logical selector must match dimension or rows/columns


# Logical Selection in array
## Matches list selection

* Logical selection in NumPy array matches list selection
* Equivalent to using `np.where` to convert boolean ot position
* Can only be directly used for 1 axis
  * Use `np.ix_` when using list/boolean in multiple dimensions


# Boolean Selection
## Summary

* Use `.loc` with boolean arrays
* Array dimension must match axis shape
* NumPy converts boolean array to list of integers
  * Care needed when selecting in 2 or more axes



# Lesson 17


# Conditional Statements
## Overview

* `if` statements allow conditional execution
* `else` extends an `if` to ensure code execution
* `elif` can be used to add additional paths
* Must use consistent indentation in `if`-`elif`-`else` blocks


# `if`

* Basic conditional statement
* Execute code in block if condition is `True`
  * Nothing executed if `False`

```python
if x >= 0:
    print(x)
```

* `if`:  Required keyword
* _condition_ is evaluated to `True`/`False`
* colon (`:`) required to end declaration
* Conditional statement **must** be consistently indented
  * **Important**: Python is whitespace sensitive
  * Use 4 spaces


# `if`-`else`

```python
if x > 0:
    print("x is positive")
else:
    print("x is negative or zero")
```

* Extends `if` statement to always execute _something_
* `else` executes if _condition_ is `False`
* `else` is dedented to same level as `if`
* Blocks end when code is dedented

```python
if x >= 0:
    print("Shown if x is non-negative")
else:
    print("Shown if x is negative")
print("Always printed: not part of conditional statement")
```


# `if`-`elif`-`else`

* `elif` allows arbitrary execution
* At most one of `if`, the `elif`s or `else` executed

```python
if x > 0:
    print("x is positive")
elif x > -1:
    print("x is not too small")
elif x > -4:
    print("x is pretty small")
else:
    print("x is very negative")
```

* Unlimited number of `elif` statements


# Conditional Statements
## Summary

* `if`-`elif`-`else` allows complete control of execution
  * `if` is required
  * `elif` and `else` are optional
* At most one of the blocks is executed
* When `else` included exactly one block is executed
* **Important**: Python is whitespace sensitive



# Lesson 18


# Logic and Loops
## Overview

* Blocks are mixed to achieve complex control flow
  * `for`
  * `if`-`elif`-`else`
* Consistent indentation is **essential**
* Best practice limits nesting to 2 or 3 levels
  * Use function to limit depth


# Nesting Blocks
## Consistent indentation

* Python uses indentation to mark compound statements
  * Function (`def`)
  * Loops (`for`/`while`)
  * Conditional Statements (`if`-`elif`-`else`)
  * Exception Handling (`try`-`except`)
  * Context managers (`with`)
* Nesting requires maintaining consistent indentation


# Complex Nesting

```python
for i in range(5):
    if i < 2:
        for j in range(7):
            def f():
                print(i,j)
            f()
            print("In the loop")
        print("If but not for")
    elif i < 4:
        print("i is in the middle of its range")
    print("Still in the loop")

print("Finished")
```
* Best practice is to limit nesting
* Good editor provide vertical guides
  * Essential in complex code


# Logic and Loops
## Summary

* Consistent indentation is **essential** when nesting blocks
* Use a good editor that highlights depth
* Limits nesting to 2 or 3 levels



# Lesson 19


# Importing Data
## Overview

* pandas exposes many methods to import data
* Readers for a wide range of formats
  * **CSV**
  * **Excel**
  * Database: SQL
  * Web: JSON and HTML
  * Statistical Software: Stata, SAS and SPSS
  * Big Data: HDF, Parquet, Feather


# Importing CSV Data
## `pd.read_csv`

* Only file name is required
```python
df = pd.read_csv('data.csv')
```
* Key optional inputs
  * `index_col`: The name of the column to set as the index
  * `parse_dates`: `True`/`False` that parses strings that look like dates
  * `skiprows`: The number of row to skip before reading data
* Dozens of optional inputs to handle most text file formats


# Importing Excel Data
## `pd.read_excel`

* Imports old (xls) and new Excel (xlsx) files
* Only file name is required
```python
df = pd.read_excel('data.xlsx')
```
* Key optional inputs
  * `index_col`: The name of the column to set as the index
  * `sheet_name`: The name of the sheet to import
  * `skiprows`: The number of row to skip before reading data
* Many other of optional inputs to import complex sheets


# Importing Data
## Summary

* Two key functions to interface with external data
  * `pd.read_csv`: CSV and other delimited text
    * `index_col` sets the index
    * `parse_dates` converts dates
  * `pd.read_excel`: Excel (xlsx and xls)
    * `index_col` sets the index
    * `sheet_name` reads from a specific sheet



# Lesson 20


# Saving and Exporting Data
## Overview

* Export formats match import
  * **CSV**
  * **Excel**
  * **HDF**: _native_ pandas format
  * Database: SQL
  * Web: JSON and HTML
  * Statistical Software: Stata and SPSS
  * Big Data: Parquet, Feather


# Saving
## CSV and Excel

* `DataFrame.to_csv` exports to CSV
```python
df.to_csv('file-name.csv')
```
* `DataFrame.to_excel` exports to Excel (xls/xlsx)
```python
df.to_excel('file-name.xlsx')
```
  * Can use `sheet_name="some name"` to specify a sheet name


# Storing HDF
## `DataFrame.to_hdf`

* Best approximation of a pandas "native" format
* Requires a file name and key
```python
df.to_hdf("data-file.h5", "df")
```
  * Overwrites existing files by default
* `mode="a"` appends additional `DataFrame`s and `Series` &nbsp;&nbsp;&nbsp;
```python
second_df.to_hdf("data-file.h5", "second_df", mode="a")
```
* Read using `pd.read_hdf`
```python
df = pd.read_hdf("data-file.h5", "df")
```


# Saving and Exporting Data
## Summary

* `df.to_csv` writes csv files
* `df.to_excel` exports to Excel
  * `sheet_name` choose the sheet name
* `df.to_hdf` output to HDF format
  * Closest format to native
  * Must set a key
  * `append=True` allows multiple variables to be saved
  * Import with `pd.read_hdf(` _filename_ `,` _key_ `)`



# Lesson 21


# Graphics: Line Plots
## Overview

* `df.plot()` produces line plots 
* `df.plot.`_method_ exposes a rich sets of visualizations
  * `line`: Line plot
  * `hist`: Histograms
  * `kde`: Kernel density
  * `scatter`: Scatter plots
  * Others: `area`, `bar`, `box`, `density`, `hexbin`, `pie`
* Wrappers around `matplotlib.pyplot`
  * Matplotlib provides core documentation for options
* `seaborn` package improves default aesthetics


# Line Plots
## `DataFrame.plot()`

* Similar to
  * `DataFrame.plot.line()`
  * `plt.plot(df.index, df.values)` 
* Key optional inputs:
  * `x`: the column name to use as the x values
  * `y`: the column names to plot
* Many optional argument that affect plot appearance
  * `linewidth`: Integer width of line
  * `linestyle`: (`"none"`, `"-""`, `"--"`, `"-."`, `":"`)
  * `marker`: Adds a marker (`"o"`, `"x"`, `"v"`,...)
  * `color`: Color (hex: `"#abcdef"`, name: `"red""` )
  * See `matplotlib.pyplot.plot` help for full list


# Graphics: Line Plots
## Summary

* `df.plot` and `df.plot.line` produces line plots
* Wrapper for `plt.plot(df.index, df.values)`
* Axis `set_`_property_ adds important features
  * `title`
  * `xlabel`, `ylabel`
* seaborn's `set_style` improves the default appearance of plots



# Lesson 22


# Graphics: Other Plots
## Overview

* Histograms
* Scatter plots
* Saving figure to common formats


# Histograms
## `DataFrame.plot.hist`

* Histogram of values
* Key optional inputs:
  * `bins`: Number of bins
  * `density`: `True`/`False` indicating whether to normalize heights to sum to 1
* Additional features available using `DataFrame.hist`
* Wrapper around `plt.hist`


# Scatter plots
## `DataFrame.plot.scatter`

* Scatter plot of two variables
* Required inputs:
  * `x`, `y`: Columns names to plot
* Key optional inputs:
  * `marker`: Marker shape (`"o"`,`"x"`,`"+"`,`"v"`,`"^"`,...)
  * `s`: Size of marker
  * `c`: Marker color
* Wrapper around `plt.scatter`


# Altering Plot Appearance

* Large set of properties available to modify
* Important properties are methods off axes
```python
ax.set_xlim(0, 1)
ax.set_xticks([0,.33,.66,1])
```
* Use pattern `ax.set_`_property_
* Key properties:
  * `xlim` and `ylim`: Set axis limits
  * `xlabel`, `ylabel` and `title`: Label a plot
  * `xticks`, `yticks`: Set location for ticks
  * `xticklabels`, `yticklabels`: Change labels of ticks
* Mirrored by `get_`_property_ to read current value


# Saving Figures
## `plt.savefig`

* Supports output to common formats
  * pdf, png, jpeg, svg
* Required inputs:
  * `fname`: filename with extension to indicate export format
* Key optional inputs:
  * `dpi`: Figure resolution in dots per inch
  * `transparent`: Use a transparent background
* Also available as a method `Figure.savefig`


# Graphics: Other Plots
## Summary

* `DataFrame.plot.hist` produces histograms
* `DataFrame.plot.scatter` produces scatter plots
  * Two required arguments: `x` and `y`
* `Figure.savefig` exports figures to common formats
  * Most useful: pdf, png, jpg, svg
  * Use fig = ax.get_figure() to get handle
* `ax.set_`_property_ allows many figure properties to be set
  * `set_xlim` and `set_ylim`
  * `set_xlabel`, `set_ylabel`, `set_title`
