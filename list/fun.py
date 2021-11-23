l=[10,20,30]
l.append(10)

l.append(9) #appending list 
print(l)
print(sorted(l)) #sorting list
print(len(l)) # length of string
print(l.count(9)) #no of occurance 
print(l.index(9)) #index, erro if not presence,check membership first
k=[1,2,2,2,3,3]
if 3 in k:
    print("it presernt at index",k.index(3))