n=int(input("for n prime numbers"))
l=[]
k=[]
for i in range(2,1000000):
    for j in range(1,i+1):
        if i%j==0:
            l.append(j)
    if l[1]==i:
        k.append(i)
    l=[] # emptying list again
    if len(k)==n:
        break

print("following are the first {} prime numbers".format(n))
print(k)