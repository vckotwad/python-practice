#using mutiple sequences
l=[1,2,3,4,5,6,7,8,9] #extra elements will be ignored
k=[45,1,24,77,2,4]
m=list(map(lambda x,y:x+y, l,k))
print(m)