from abc import abstractmethod,ABC
class vehicles(ABC):  #interface when all methods in abstract class are abstract methods
    @abstractmethod
    def wheels(self):
        pass
class bus(vehicles):
    def wheels(self):
        return 4
class auto(vehicles):
    def wheels(self):
        return 3
b=bus()
print(b.wheels())
a=auto()
print(a.wheels())
