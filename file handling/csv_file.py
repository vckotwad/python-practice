#writting into csv file
import csv
with open('emp.csv','w',newline="") as f:
    w=csv.writer(f)
    l=['name','sal']
    w.writerow(l)
    while True:
        name=input("enter name")
        sal=int(input("enter salary"))
        w.writerow([name,sal])
        break
print("data writting completed")