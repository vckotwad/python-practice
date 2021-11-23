#adding name marks into dict
d={}
while True:
    n=input("enter the name")
    m=int(input("enter marks"))
    d[n]=m
    q=input("do you want to add more Y or n")
    if q=='n':
        break

print(d)