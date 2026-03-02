import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left' )

    return df[df['customerId'].isna()].rename(columns={'name':'Customers'})[['Customers']]