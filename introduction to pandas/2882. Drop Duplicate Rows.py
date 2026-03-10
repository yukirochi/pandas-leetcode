import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(customers)
    df.drop_duplicates(subset=['email'],keep='first', inplace=True)
    return df