def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub #return mutiple values in the form single tuple
x,y=sum_sub(20,10) # save in different variables

print("sum is", x)
print("sub is",y)
t=sum_sub(40,20)
print(type(t))
print(t) 