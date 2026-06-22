# Boolean Series for Filtering in Pandas

## What it is
- A boolean Series is a Series with `True`/`False` values
- Must have the same index as the DataFrame you're filtering

## How it works
```python
# Create boolean mask
mask = df['column'].str.match(pattern)  # or any condition

# Filter DataFrame
filtered_df = df[mask]  # Keeps rows where mask is True
```

## My solution
```python
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    email_regex = "^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$"
    filtered_emails = users["mail"].str.match(email_regex)
    return users[filtered_emails]
```
