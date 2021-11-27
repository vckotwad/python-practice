#try with single exception block
try:
    x=int(input("enter the first number"))

    y=int(input("enter the second number"))
    print(x/y)
except (ZeroDivisionError,ValueError) as msg:   
    print("exception type:_ ",type(msg))
    print('description of error is :- ',msg)
   

