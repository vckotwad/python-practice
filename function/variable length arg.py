'''
def f(*n): # n act as a tuple 
    print(type(n))
    print(n)
f()
f(1,2,3,4,5)
'''
'''
def add(*n): # providing mutiple values
    sum=0
    for i in n: #iterating each value in tuple
        sum=sum+i
    print("sum is equal to",sum)
add(1,2,4,5,13,3,5,6,1,34,3,5,4)
'''
def fun1(*y,x): #passing one normal argument and variable length argument
    print(x)
    for i in y:
        print("value of y is", i)

fun1(19,23,5,3,32,x=34) #normal keyword arg should be at the end