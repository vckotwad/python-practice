#heierarchical inheritance, one parent, multiple childs
print("this is hierarchical inheritance")
class p:
    def m1(self):
        print("this parent method")
class c1(p):
    def m2(self):
        print("this child 1 method")
class c2(p):
    def m3(self):
        print("this child 2 method")
child1=c1()
child2=c2()
child1.m1()
child1.m2()
child2.m1()
child2.m3()