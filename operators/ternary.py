#takes three operands
#x= First value IF condition ELSE second value
a=int(input("enter a value")) # input always get str value
b=int(input("enter another value"))
c=a if a<b else b
print("min value is ", c)