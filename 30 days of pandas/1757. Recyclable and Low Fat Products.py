import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(products)

    return df[(df['low_fats'] == 'Y') & (df['recyclable'] == 'Y')][['product_id']]