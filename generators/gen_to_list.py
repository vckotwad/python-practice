# gen to list conversion
n=int(input("enter the number")) 

def gen(n):
    i=0
    while i<=n:
        yield i
        i+=1


g=gen(n)
l=list(g)
print(l)

