import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(views)

    return df[df['author_id'] == df['viewer_id']].rename(columns={'author_id':'id'})[['id']].sort_values(by='id').drop_duplicates(subset=['id'])



