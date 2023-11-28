import numpy as np 
import pandas as pd 


random_data = np.random.randint(1 , 101, [3, 5])


cities = pd.DataFrame(data = random_data)


print(cities)

