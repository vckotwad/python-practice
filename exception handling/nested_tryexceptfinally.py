#nested try except finally
try:
    print("this is outer try block")
    try:  #inner try except finnaly block
        print("this is inner try block")
        print(10/0)
    except ValueError: #if inner except block could not handle exception then control goes to outer except block
        print("this is inner except block")
    finally:
        print("this is inner finnaly block")
except ZeroDivisionError:
    print("this is outer except block")
    
finally:
    print("this is outer finally block")