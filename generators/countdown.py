from time import sleep
n=int(input("enter the countdown number"))
def count(n):
    while n>=0:
        yield n
        n=n-1

g=count(n)   #values stored at g one at a time 
for x in g:  #for is used for next values
    print(x)
    sleep(1)
