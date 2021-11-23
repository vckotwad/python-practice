'''
def f1(**kwargs): # keyword variable length
    print(kwargs) # print dictionaly of key value

f1(a=10, b=20)
'''
def f2(*x, **y): #simultenously using, first *args only after **kwargs
    print(x) # x becomes tuple 
    print(y) # y becomes dictionary
f2(10,19,12,a=12,b=14,c=15)