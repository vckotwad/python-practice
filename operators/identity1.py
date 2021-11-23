#object reusability is not there in list dict etc
l1=[10,20,30,40]
l2=[10,20,30,40]
print(id(l1)) # different addresses
print(id(l2))
print(l1 is l2) #object comparison checks address
print(l1==l2) # content comparison