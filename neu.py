import numpy as np 
import pandas as pd 


city_data = {
    "City": ["NYC", "Paris", "Rome"],
    "Country": ["US", "France", "Italy"],
    "Population": [8600000, 2141000, 2873000]
}


cities = pd.DataFrame(city_data)

print(cities)