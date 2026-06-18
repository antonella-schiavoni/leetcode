import pandas as pd

---

Every `world['column']` call returns a pandas **Series**, which carries an index.
Before the `|` can run, pandas **aligns the two Series by index** — even though they're from the same DataFrame and alignment is trivially a no-op here, the check still happens.
You also hit the DataFrame twice: once to filter rows, once to select columns.

```python
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # First submission. Runtime 308ms
    # Multiple conditions (use & for AND, | for OR)
    filtered_df = world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]
    return filtered_df[['name', 'population', 'area']]
```

---

`query()` parses the string and, for large DataFrames, delegates to **numexpr**, which evaluates the expression in chunks without building two full boolean Series in memory first.
That's the win. The tradeoff is string parsing overhead, which hurts on small data. Column selection is still a second step.

```python
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Second submission. Runtime 293ms
    return world.query('population >= 25_000_000 or area >= 3_000_000')[['name', 'population', 'area']]
```

---

`.values` drops you down to a raw **numpy array** — no index, no alignment check, pure C-level comparison.
The `|` runs on numpy booleans, not pandas Series. Then `.loc[mask, cols]` filters rows and selects columns in a single pass instead of two.

```python
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Third submission. Runtime 271ms
    mask = (world['population'].values >= 25_000_000) | (world['area'].values >= 3_000_000)
    return world.loc[mask, ['name', 'population', 'area']]
```

---

**The two core concepts:**

| Concept | What it means |
|---|---|
| **Index alignment overhead** | pandas always checks that two Series indexes match before operating on them — numpy arrays have no index, so `.values` skips this |
| **Chained indexing vs `.loc`** | `df[mask][cols]` is two separate operations; `df.loc[mask, cols]` is one — and `.loc` is also safer (avoids `SettingWithCopyWarning`) |
