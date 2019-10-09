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

* Modern text editor
* Supports extensions to add features
  * First-class Python provided by Microsoft
* Supports importing and exporting Jupyter notebooks
* Restricted support for Markdown cells



# VS Code
## Summary

* First-class support for Python provided by Microsoft
* Jupyter notebooks must be imported to use
  * Must be exported to share
* Relies on Magic Python cells 
  * Cells demarcated with `#%%`
* Limited support for Markdown cells
  * Must comment all lines or use multi-line string
```python
"""
# Markdown
This is a multi-line cell containing Markdown
content in VS Code.
"""
```   



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



# Creating `DataFrame`
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

* Each column of a `DataFrame` is a Seris
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
# Overview

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
def func(x):
    function code
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
# Summary

* Function begin with `def`
* Returned value uses `return`
* Function code is indented
  * **Important**: Python is white-space sensitive
  * Use 4 spaces to indent
    * Do not use tab character to indent
    * Configure editor to convert tab to 4 spaces 
