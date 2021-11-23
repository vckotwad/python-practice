#wpa to remove duplicate present in the list
l=[1,2,2,3,4,5,5,6,7,8,8,8,9,9]
print(l)
s=set(l)
print(s)
l=list(s)
print(l)


#other approach
l=[1,2,2,3,4,5,5,6,7,8,8,8,9,9]
print(l)
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)

print(l1)