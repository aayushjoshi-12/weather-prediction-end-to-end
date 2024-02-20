import pandas as pd

def create_features(df : pd.DataFrame) -> pd.DataFrame:
    """
    Creates time series feature from datetime index such as hour, day, month, year.
    """
    df = df.copy()
    df['date'] = df.index.date
    df['month'] = df.index.month
    df['year'] = df.index.year  
    df['hour'] = df.index.hour
    return df