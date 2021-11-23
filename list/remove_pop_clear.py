l=list(range(1,11))
l2=[10,10,10,10,10]
l.extend(l2)
print(l)
if 10 in l:
    l.remove(10) #only first occurance of 10 only
print(l)
l.pop() #remove last element only, index error when list empty. 
print(l)
while 10 in l:
    l.remove(10)
print(l)

l.clear()
print(l)