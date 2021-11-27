#try with multiple exception 
try:
    x=int(input("enter the first number"))

    y=int(input("enter the second number"))
    print(x/y)
except ZeroDivisionError as z:    #order of except bloc also important
    print('error is ',z)
    print("you can not divide by zero")

except ValueError as v:
    print(v)
    print("please enter value in digit")
    