#mro

class a:
    pass
class b(a):
    pass
class c(a):
    pass
class d(b,c):
    pass
print(d.mro()) #this will give the mro of method 
