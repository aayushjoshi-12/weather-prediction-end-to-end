import pandas as pd
from meteostat import Point, Hourly
from datetime import datetime

# use os/sys so that the dataset is saved in the correct location

location = Point(29.9155421, 78.0955212) # we gonna use geopy to fetch this later or can create a system using meteostat only by giving hte closest location

def collect_data(location: Point, time_period = 3) -> pd.DataFrame:
    """
    Collects weather data from Meteostat API for a given location and time period.
    Args:
    - location: meteostat.Point
    - time_period: int, default 5 years
    """
    start_date = datetime(datetime.now().year - time_period, datetime.now().month, datetime.now().day)
    end_date = datetime.now()
    data = Hourly(location, start_date, end_date)
    # print(data.coverage()) # this is not working properly
    data = data.fetch() # use try catch later to avoid errors
    data.to_csv('dataset/raw_dataset.csv')

    return data

if __name__ == '__main__':
    collect_data(location)
    print('Data collected and saved to dataset/raw_dataset.csv')