s={}
print(type(s)) #dict type but not set
p=set() # creating empty set
print(type(p))
p.add(10) #add but no append due to order
p.add(10) #no duplicates
print(p)
p.add('z')
p.add('a')
print(p) #no order

# p.[1:3] no indexing no order
p.remove(10)
print(p)


