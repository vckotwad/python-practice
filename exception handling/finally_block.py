#finally block
import os
try:
    print("print try block")
    #os._exit(0) if this line executes then finally wont execute
    print(10/0)
except ValueError:
    print("you can not divide by zero")
finally: # finally block will be executed even in case of exception not handled
    print("this is finally block") 