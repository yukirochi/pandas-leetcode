import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students)

    filtered = df.loc[df['student_id'] == 101] 
    return filtered.drop(columns = ['student_id'])
    