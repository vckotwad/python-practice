a=int(input("enter a value"))
b=int(input("enter a value"))
result="both are equal" if a==b else "{} is greater than {}".format(a,b) if a>b else "{} greater than {}".format(b,a)
print(result)