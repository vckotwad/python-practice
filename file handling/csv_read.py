#readin data from csv

import csv
with open('emp.csv','r') as f:
    r=csv.reader(f)
    data=list(r)
print(data)