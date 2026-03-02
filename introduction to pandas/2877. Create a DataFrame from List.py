import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = pd.DataFrame(players)
    total_rows = df.shape[0]
    total_column = df.shape[1]
    
    return [total_rows, total_column]   