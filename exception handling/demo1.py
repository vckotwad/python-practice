#exception handling 
#BaseException will handle all the exceptions under it. 
print("hello")
try:
    print(10/0) #risky code
except BaseException as msg: #must know the name of error # using msg as reference variable to error
    print("type of error",type(msg)) #printing the type of error.
    print("type of error",msg.__class__)
    print(10/2) #alternative code
print("hi")