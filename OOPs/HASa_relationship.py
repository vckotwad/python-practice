#has a relationship

class engine:
    def engine_fun(self):
        print("engine functionality")
        self.power="100_PSI"

class car:
    def __init__(self):
        print("car object is created")
        self.engine=engine()
        print("car has a engine")

    def car_fun(self):
        print("car functionality")
        self.engine.engine_fun()
        print(self.engine.power)

c=car()
c.car_fun()