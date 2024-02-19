from meteostat import Point, Hourly
from datetime import datetime


location = Point(29.9155421, 78.0955212)
start_date = datetime(2024, 1, 1)
end_date = datetime.now()

data = Hourly(location, start_date, end_date)
data = data.fetch()
data.to_csv('dataset/dataset.csv')