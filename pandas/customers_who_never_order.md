## Find customers with no orders

```python
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers.merge(orders, left_on="id", right_on="customerId", how="left")
    no_orders = result.loc[result["customerId"].isna(), ["name"]]
    return no_orders.rename(columns={"name": "Customers"})
