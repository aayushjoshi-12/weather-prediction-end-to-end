import pandas as pd
from datetime import datetime

def create_features(df : pd.DataFrame) -> pd.DataFrame:
    """
    Creates time series feature from datetime index such as hour, day, month, year.
    args:
    - df: pd.DataFrame
    """
    df = df.copy()
    df['date'] = df.index.date
    df['month'] = df.index.month
    df['year'] = df.index.year  
    df['hour'] = df.index.hour

    return df

def train_test_split(df, features, labels, test_size = 1) -> tuple:
    """
    Splits the dataset into training and testing sets.
    args:
    - df: pd.DataFrame
    - features: list
    - labels: list
    - test_size: int, default 1 year    
    """
    start_date = datetime(datetime.now().year - 5, datetime.now().month, datetime.now().day)
    split_date = datetime(datetime.now().year - test_size, datetime.now().month, datetime.now().day)
    end_date = datetime.now()

    X_train = df.loc[start_date:split_date][features]
    X_test = df.loc[split_date:end_date][features]
    y_train = df.loc[start_date:split_date][labels]
    y_test = df.loc[split_date:end_date][labels]

    return X_train, X_test, y_train, y_test