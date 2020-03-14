# files available at C:\Users\Mfornaroli\Downloads\python_with_pandas
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np

data_with_headers = r'C:\Users\Mfornaroli\Downloads\python_with_pandas\data_with_headers.csv'
data_file = pd.read_csv(data_with_headers)

print(data_file[0:3])

time = data_file['time']
print(time[0:9])
sensors = data_file.loc[:,'s1' : 's4']   #diamo in inpur righe e colonne.. crea sottoinsieme dataframe

print(sensors[0:6])

# sensors = data_file.loc[1:2 ,'s1' : 's4']
# print(sensors)

time = time - time[0]
print(type(sensors))

avg_row = np.mean(sensors, 1)
avg_col = np.mean(sensors, 0)

print(avg_row[0:3])
print(avg_col[0:3])

print(avg_row)
print(avg_col)
