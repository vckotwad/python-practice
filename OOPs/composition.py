#composition strong association, 
class university:
    def __init__(self):
        print("university object created")
        self.department=self.department()
    class department: # class department can not exist without university
        def __init__(self):
            print("department object createdd")     
a=university()