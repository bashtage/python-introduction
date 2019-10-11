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



# Logic and Loops
## Overview

* `if`-`else` blocks
* Using boolean values as 0-1 integers
* Selection from arrays using booleans
* `where` and integer selection
* `any` and `all` 



# Logic and Loops
## Summary

* `if`-`else` blocks allow code to conditionally execute
  * Extendable using multiple `elif` statements
* Boolean `True` is 1 and `False` is 0
  * Multiplication treats boolean as an indicator
* Boolean Series can be used to select elements using `loc`
* `np.where` returns the indices where a Series is `True`
* `any` and `all` aggregate boolean values
  * `np.any` is different from `DataFrame.any`



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



# Spyder
## Overview

* Native Python development environment
* Included in Anaconda
* Most friendly for beginners
* **No** native support for Jupyter notebooks



  
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



# `Series` and `DataFrames`
## Summary

* A `Series` is a 1-d homogeneous array
* A `DataFrame` is a 2-d heterogeneous array
  * A `Series` is 1 column from a `DataFrame` 
* The `index` contains a set of keys corresponding to rows
* `DataFrame` supports keys for columns as well (`columns`)
  * `Series` supports `name` since always 1 column  



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



# `DataFrames` from `Series`
## Summary

* Build `DataFrame` from `Series`
  * `Series` as rows using a list
  * `Series` as columns using a dictionary



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



# Line Plots
## `DataFrame.plot.line`

* Same as `plt.plot(df.index, df.values)`
* Key optional inputs:
  * `x`: the column name to use as the x values
  * `y`: the column names to plot
* Many optional argument that affect plot appearance
  * `linewdith`: Integer width of line
  * `linstyle`: (`"none"`, `"-""`, `"--"`, `"-."`, `":"`)
  * `marker`: Adds a marker (`"o"`, `"x"`, `"v"`,...)
  * `color`: Color (hex: `"#abcdef"`, name: `"red""` )
  * See `matplotlib.pyplot.plot` help for full list




# Graphics: Other Plots
## Overview

* Histograms
* Scatter plots
* Saving figure to common formats




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




# pandas `DataFrame`
## Heterogeneous 2-d arrays

* Something...



# pandas `Series`
## Homogeneous 1-d arrays

* Each column of a `DataFrame` is a `Series`
* Constructed using
```python
pd.Series([1,2,3])
```
* Optional arguments
  * `index` is the index for the `Series`
  * `name` is same as the column name in a `DataFrame`



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
* May also take additional inputs
* Important examples
  * NumPy arrays
  * pandas `DataFrames` and `Series` all
* Called using `.`_function_ syntax
```python
a = np.array([1, 2, 3])
a.mean()
a.reshape((3, 1))
```



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



# Altering Plot Appearance

* Large set of figure properties available
* Mode important are methods off an axis
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



# pandas `Series`

* Building block of pandas `DataFrame`
* Homogeneous
  * `int`, `float`, `datatime`, `str`
* Handle missing values
* Support non-numeric indexing
  * Dates, Company Name, ...
* Provide many common statistical operations
  * Mean, Standard Deviation, Variance
  * Skewness and Kurtosis
  * Quantile
* Operations ignore missing values by default



# Constructing  a `Series`

* Series constructed from lists
```python
s = pd.Series([1.0, 2.0, 3.0])
```
* Key optional inputs
  * `index`: Set the index for the Series &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  * `name`: The series' name
```python
idx = ["a", "b", 'c']
s = pd.Series([1.0, 2.0, 3.0], index=idx, name="data")
```



# Custom Functions
## Overview

* Custom functions simplify repetitive code
* Required in some applications
  * Function optimization
  * Numerical integration
* Begin with keyword `def`
* End when indentation level return to previous level
* **Important**: Python is white-space sensitive



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
  * **Important**: Python is white-space sensitive
  * Use 4 spaces to indent
    * Do not use tab character to indent
    * Configure editor to convert tab to 4 spaces 



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



# Selection in `DataFrames`
## Overview

* Two ways to select using index values or column names
  * `.loc[`_rows_ `,`_cols_ `]`
  * Dictionary-like syntax
    * Selects columns in a `DataFrame`
    * Selects index in a `Series`
* Selection _may_ reduce dimension and change type    
* Special features for selecting dates
  * Day, Month, Year
  * Continuous range of dates    



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



# `DataFrame.loc`
## Selection by index and column

* `.loc[`_rows_ `,`_cols_ `]`
  * _rows_ contains element(s) from `index`
  * _columns_ contains element(s) from `columns`
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
* List selection also preserves dimension in `Series`



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


# Accessing Elements in NumPy Arrays
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


# Accessing Elements in NumPy Arrays
## Summary

* Three methods to select elements
  * Scalar
  * Slice
  * Lists of integers
* Can mix the difference selectors
  * Should only use 1 list unless using `ix_`
  


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
