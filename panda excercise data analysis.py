# files available at C:\Users\Mfornaroli\Downloads\python_with_pandas
import pandas as pd
import numpy as np


data_with_headers = r'C:\Users\Mfornaroli\Downloads\python_with_pandas\data_with_headers.csv'
data_file = pd.read_csv(data_with_headers)
print("\n")
print(data_file[0:3])
time = data_file['time']
print("\n")
print(time[0:9])
sensors = data_file.loc[:,'s1' : 's4']
print("\n")                                         # diamo in inpur righe e colonne.. crea sottoinsieme dataframe
print(sensors[0:6])
time = time - time[0]
print("\n")
print(type(sensors))

avg_row = np.mean(sensors, 1)
avg_col = np.mean(sensors, 0)
print("\n")
print(avg_row[0:3])
print(avg_col[0:3])
print("\n")
print(avg_row)
print(avg_col)
print("\n")
my_data = [time, sensors, avg_row]
result = pd.concat(my_data, axis = 1)
print(result[0:3])

result.to_csv(r'C:\Users\Mfornaroli\Downloads\python_with_pandas\risultati_in_csv.csv')
# result.to_excel(r'C:\Users\Mfornaroli\Downloads\python_with_pandas\risultati_in_excel.xlsx')

import matplotlib.pyplot as plt

plt.plot(time,  sensors['s1'], 'r-')
plt.plot(time, avg_row, 'b.')
plt.legend(['sensor1', 'sensor2'])




