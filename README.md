# README #

This README would normally document whatever steps are necessary to get your application up and running.

### Contribution guidelines ###

Please put all csv, zip and bz2 files to 'data' dir and keep all your notebooks and scripts inside your current user directory

### Connection guidelines ###

### helper.py functions ###

helper.py designed to help in modifiying dataframe with features.

* method sort_df_cols_by:
```python
import sys
import re
sys.path.insert('../eugtsa/')
from helper import sort_df_cols_by

#...
X_sorted = sort_df_cols_by(X_unsorted, match_to_sort=re.compile(r'.[1-5]_xp'))
#...

# match_to_sort regexp should match only one feature type in all heroes
```
