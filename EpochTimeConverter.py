import pandas as pd
from datetime import datetime

list2 = []
list1 = []

file = pd.read_csv('file location here', header=None)
date = pd.to_datetime(file[0], unit='s')

for i in range(len(file)):
    list1.append(file[1][i])

for i in range(len(date)):
    list2.append(date[i])

res = "\n".join("{} {}".format(y, x) for x, y in zip(list1, list2))
print(res)