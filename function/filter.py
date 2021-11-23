#without filter function 

'''
even=[]
odd=[]
def iseven(l):
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

m=[0,1,2,3,4,5,6,7,8,9,10,11,12]
iseven(m)
print(even)
print(odd)
'''
'''
#without using filter function 
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9,10]
k=[]
for i in l:
    if iseven(i)==True:
        k.append(i)

print(k)        
'''
'''
#by using filter funciton 
q=list(filter(iseven,l)) #for every value in l, if return true then add to the list
print(q)
'''
'''
w=list(filter((lambda i:i%2!=0 ), range(1,101)))
print(w)
'''
x=list(filter((lambda i:(i%3)==0 and (i%2)!=0),range(1,101)))
print(x)
