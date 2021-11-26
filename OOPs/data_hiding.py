#data hiding
class test:
    def __init__(self,balance):
        self.__balance=balance
    def info(self):
        #authentication and validation
        return self.__balance
t=test(1000)
print(t.info())
    