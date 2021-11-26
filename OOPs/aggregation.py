#aggregation weak association
class department:
    def __init__(self,prof):
        print("department object is created")
        self.prof=prof

class prof: #professor can exist without department
    def __init__(self):
        print("professor object is created")

prof=prof()
it=department(prof)
