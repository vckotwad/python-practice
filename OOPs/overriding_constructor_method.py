#overriding
class p:
    def __init__(self):
        print("parent constructor")
    def m1(self):
        print("parent method")
class c(p):
    def __init__(self): #constructor overriding
        print("child constructor")
    def m1(self): #method overriding
        print("child method")
C=c()
C.m1()