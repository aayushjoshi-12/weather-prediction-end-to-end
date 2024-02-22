import pandas as pd
from meteostat import Point, Hourly
from datetime import datetime
from geopy.geocoders import Nominatim

place = "Arlington, Virginia" # we will later create a better input system to get the location of a place 

def find_lat_lon(place : str) -> Point:
    """
    Finds latitude and longitude of the given place.\n
    Args:
    - place : str 
    """
    locator = Nominatim(user_agent="weather-prediction-end-to-end")
    location = locator.geocode(place)
    if location is None:
        raise ValueError('Location not found')
    else:
        return Point(location.latitude, location.longitude)


# use os/sys so that the dataset is saved in the correct location

def collect_data(location: Point, time_period = 5) -> pd.DataFrame:
    """
    Collects weather data from Meteostat API for a given location and time period.\n
    Args:
    - location: meteostat.Point
    - time_period: int, default 5 years
    """
    start_date = datetime(datetime.now().year - time_period, datetime.now().month, datetime.now().day)
    end_date = datetime.now()
    
    # decide where to start collecting data from and according to that create the train test split 
    # try to come up with a way where you can come up with the start date and end date according to the data availability 

    try:
        print('Fetching data...')
        data = Hourly(location, start_date, end_date)
        data = data.normalize().interpolate()
        data = data.fetch() 
    except:
        print('Data not found')
        exit()

    data.to_csv('dataset/raw_dataset.csv')
    return data

if __name__ == '__main__':
    try : 
        location = find_lat_lon(place)
    except ValueError:
        print('Location not found')
        exit()

    data = collect_data(location)
    print('Data collected and saved to dataset/raw_dataset.csv')