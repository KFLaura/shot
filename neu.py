import numpy as np 
import pandas as pd 


random_data = np.random.randint(1 , 101, [3, 5])

row_labels = ["ROW 1", "ROW 2", "ROW 3"]

coloumn_labels = ("COLUMN 1", "COLUMN 2", "COLUMN 3", "COLUMN 4", "COLUMN 5")

data_frame_test = pd.DataFrame(data = random_data, index = row_labels, columns = coloumn_labels)


print(data_frame_test)

