'''
s=input("enter a number ")
print(s)
l=s.split()
print(l)
l1=[int(x) for x in l]
print(l1)
a,b=l1
print(a)
print(b)
'''
#muitple input using split method
a,b,c = [float(x) for x in input("enter 3 num").split(',')]
print(a)
print(b)
print(c)
print("sum is", a+b+c)