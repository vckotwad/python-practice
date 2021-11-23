c=0
def fact(n):
    global c
    c=c+1
    print("factorial of", n)
    if n==0:
        result=1
    else:
        result=n*fact(n-1) #function calling itself
        print("excecutin factorial of ", n, "having result",result)
        
    return result
    print("excecutin factorial of ", n, "having result",result)
print(fact(996))
print("recusion count is",c)