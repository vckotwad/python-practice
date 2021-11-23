print(10==20)
print(10!=20)
print(1==True)
print(1!=False)
print('vaibhav'=='vaibhav')
print(10=='vaibhav')

print('chaining of equality operator') # if all true then true
print(10==10==20)


print(" use of is vs ==")

l1=[10,20,30]
l2=[10,20,30]
l3=l1 # l3 and l1 pointing to same object
print(id(l1))
print(id(l2))
print(l1 is l2) # is = meant for reference to same object

print(l1==l2) # == content comparison

print("l3 and l1")
print(l1 is l3)