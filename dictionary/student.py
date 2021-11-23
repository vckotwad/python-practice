d={}
n=1
while n==1:
    x=input("please enter name")
    y=input("enter marks of student")
    d[x]=y
    n=n+1

z=input("enter name of the student")
print("marks of {} is {}".format(z,d.get(z)))
