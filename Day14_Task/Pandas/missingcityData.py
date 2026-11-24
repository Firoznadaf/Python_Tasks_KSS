#  Missing City Data (NaN Handling) 

import pandas as pd

cities = {
    "Delhi": 2000000,
    "Mumbai": 3000000, 
    "Chennai": 1500000
}

my_cities = ["Delhi", "Chennai", "Bangalore"]

city_series = pd.Series(cities, index=my_cities)

print(city_series)

# check missing value
print("\nMissing values:")
print(city_series.isnull())