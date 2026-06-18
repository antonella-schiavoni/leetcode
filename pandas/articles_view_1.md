```python

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask = (views['author_id'] == views['viewer_id'])
    authors_viewers = views.loc[mask, ['author_id']]
    dedup_authors = authors_viewers.drop_duplicates(subset=["author_id"])
    dedup_authors = dedup_authors.rename(columns={"author_id": "id"})
    return dedup_authors.sort_values("id")
```

```python
import numpy as np
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = views.loc[views["author_id"] == views["viewer_id"], "author_id"]
    return pd.DataFrame({"id": np.sort(ids.unique())})
```
## What changed and why

**1. Extract a Series instead of a DataFrame**
`views.loc[mask, ['author_id']]` (double brackets) returns a DataFrame.
`views.loc[mask, 'author_id']` (single) returns a Series.
A Series is lighter — no column index, less memory, faster downstream operations.

**2. `.unique()` instead of `.drop_duplicates()`**
`drop_duplicates` is designed for DataFrames and carries overhead even on a single column.
`.unique()` on a Series returns a raw NumPy array directly — no pandas wrapping, faster for this use case.

**3. `np.sort()` instead of `.sort_values()`**
`.sort_values()` operates on a pandas DataFrame and returns one.
`np.sort()` operates on the NumPy array returned by `.unique()` and stays in NumPy land — no pandas overhead.

**4. Build the result in one shot**
The original creates multiple intermediate DataFrames (filter → dedup → rename → sort).
The optimized version builds the final DataFrame once, skipping the rename step entirely.
