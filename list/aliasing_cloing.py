l1=list(range(1,11))
l2=l1
l2.pop() #l2 affecting l1
print(l1)

#cloinng by copy method or slice opr
#slicing method
s=list(range(1,10))
s1=s[::]
print(id(s),id(s1))
s1.pop()
print(s)
l3=l2.copy() #cloning l2 so not affecting l2
l3.pop()
print(l2)