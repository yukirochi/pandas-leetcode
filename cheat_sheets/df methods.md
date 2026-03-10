# Pandas Insight Series 🔥 (Enhanced Edition)

## 1. Basic Attributes (Properties)
*Attributes do not use parentheses `()`.*

- `df.shape`
  - Returns a tuple `(rows, columns)` representing dimensionality.
- `df.columns`
  - Returns a list of column labels.
- `df.index`
  - Returns the row labels.
- `df.dtypes`
  - Returns the data type (int64, float64, object/string) of each column.

## 2. Basic Methods (Inspection)

- `df.info(verbose=True, show_counts=True)`
  - **Args:** `show_counts=True` shows non-null count per column (useful for large datasets).
- `df.head(n=5)` / `df.tail(n=5)`
  - **Args:** `n`: Number of rows to return.
- `df.describe(include='all', percentiles=[.05, .95])`
  - **Args:** `include='all'` (summarizes string columns too), `percentiles` (custom stats).
- `df.count()`
  - Counts non-NA cells for each column or row.

## 3. Dropping Data

- `df.drop(labels=['col1'], axis=1, inplace=False)`
  - **Args:**
    - `axis=1` (columns) or `axis=0` (rows).
    - `inplace=True`: Modifies existing DF. `False`: Returns a copy.
    - `labels`: The name of the row or column to drop.

## 4. Handling Missing Data

- `df.isna().sum()`
  - Detects missing values and chains `.sum()` to count them per column.
- `df.dropna(axis=0, how='any', subset=['col1'], inplace=False)`
  - **Args:**
    - `how='any'`: Drop if *any* NaN present. `how='all'`: Drop only if *entire* row is NaN.
    - `subset=['col']`: Only check specific columns for NaNs.
- `df.fillna(value=0, method='ffill', inplace=False)`
  - **Args:**
    - `value`: The specific value to replace NaNs with (e.g., 0, "Unknown").
    - `method='ffill'` (forward fill) or `'bfill'` (backward fill).

## 5. Data Manipulation

- `df.sort_values(by=['col1', 'col2'], ascending=[False, True], inplace=False)`
  - **Args:**
    - `by`: Single column or list of columns.
    - `ascending=False`: Sorts High -> Low.
- `df.rename(columns={'old': 'new'}, index={0: 'start'}, inplace=False)`
  - **Args:** Use `columns=` dict for headers, `index=` dict for row labels.
- `df.astype({'col1': 'int32'})`
  - **Args:** Pass a dictionary to cast multiple columns at once. **No inplace**.
- `df.drop_duplicates(subset=['email'], keep='first', inplace=False)`
  - **Args:**
    - `subset`: Column(s) to check for duplicates.
    - `keep='last'`: Keeps the last occurrence. `keep=False`: Drops *all* duplicates.
- `df.reset_index(drop=True, inplace=False)`
  - **Args:** `drop=True`: Discards the old index instead of adding it as a new column.

## 6. Grouping and Aggregation

- `df.groupby(by='col', as_index=False).mean()`
  - **Args:** `as_index=False`: Critical! Keeps the grouped column as a regular column (SQL style) rather than making it the index.
- `df.value_counts(normalize=True, dropna=False)`
  - **Args:**
    - `normalize=True`: Returns **percentages** instead of raw counts.
    - `dropna=False`: Counts missing values (NaN) as a category.
- `df.nunique(axis=0)`
  - Counts number of distinct elements in specified axis.

## 7. Merging and Joining

- `pd.concat([df1, df2], axis=0, ignore_index=True)`
  - **Args:**
    - `axis=0`: Stack vertically (add rows). `axis=1`: Stack horizontally (add cols).
    - `ignore_index=True`: Resets index 0 to N after stacking.
- `pd.merge(df1, df2, on='key', how='inner', suffixes=('_left', '_right'))`
  - **Args:**
    - `how`: `'left'`, `'right'`, `'outer'`, `'inner'`.
    - `on`: Column name shared by both.
    - `left_on` / `right_on`: Use if column names differ (e.g., `id` vs `customer_id`).

## 8. Function Application

- `df.apply(func, axis=1)`
  - **Args:** `axis=1`: Applies function row-by-row. `axis=0`: Column-by-column.
- `df.map(func)`
  - **Args:** Applies function element-wise (to every single cell). *Note: Replaces `applymap` in Pandas 2.1+.*

## 9. String Manipulation (Series)
*Access via `.str` accessor.*

- `df['col'].str.contains('pattern', case=False, na=False)`
  - **Args:** `case=False` (ignore case), `na=False` (treat missing values as False).
- `df['col'].str.lower()`
  - Converts strings in the Series to lowercase.
- `df['col'].str.replace('old', 'new', regex=True)`
  - **Args:** `regex=True`: Allows use of Regular Expressions for complex patterns.

## 10. Input/Output

- `pd.read_csv('path', usecols=['A', 'B'], parse_dates=['date_col'])`
  - **Args:**
    - `usecols`: Read only specific columns (saves memory).
    - `parse_dates`: Automatically convert columns to datetime objects.
- `df.to_csv('path', index=False)`
  - **Args:** `index=False`: **Crucial.** Prevents writing the row numbers (0, 1, 2...) into the file.