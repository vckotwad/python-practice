#creating inner class
class outer:
    def __init__(self):
        print("outer class object creation")

    class inner:
        def __init__(self):
            print("inner class object is created")

        class innerinner:
            def __init__(self):
                print("nested inner class objct is created")
            def m1(self):
                print("nested inner class method is called")

        

outer().inner().innerinner().m1()

# outer().inner().m1() also works by combining above 3 lines 

