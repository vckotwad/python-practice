a=int(input("enter a value"))
b=int(input("enter a value"))
c=int(input("enter a value"))
d=int(input("enter a value"))
e=a if a<b and a<c and a<d else b if b<c and b<d else c if c<d else d
print("min value is ", e)