import pickle
class employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("eno:{},ename:{},esal:{},eaddr:{}".format(self.eno,self.ename,self.esal,self.eaddr))
e=employee(100,'durga',1000,'pune')
#serilisation
with open('emp.ser','wb') as f:
    pickle.dump(e,f)
print("serilisation complete")

with open('emp.ser','rb') as file:
    obj=pickle.load(file)

print(obj.display())
