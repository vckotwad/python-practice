n=int(input("enter the number"))
l=[]
k=[]
for i in range(2,n+1):
    for j in range(1,i+1):
        if i%j==0:
            l.append(j)
    if l[1]==i:
        k.append(i)
    l=[]
print(k)
            
