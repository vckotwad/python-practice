#using regular method
'''
i=0
j=1
n=int(input("enter the n value"))
while n>0:
    k=i+j
    print(k)
    i=j
    j=k
    n=n-1

'''

def fib(n):
    i=0
    j=1
    while n>0:
        k=i+j
        yield k
        i=j
        j=k
        n=n-1


n=int(input("enter n value"))
g=fib(n)
for x in g:
    print(x)