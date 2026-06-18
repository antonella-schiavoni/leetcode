```python
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = (products['low_fats'].values == 'Y') & (products['recyclable'].values == 'Y')
    return products.loc[mask, ['product_id']]
