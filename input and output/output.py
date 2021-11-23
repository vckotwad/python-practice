from os import name


print("vaibhav")
print()
print("vaibhav\t\tvaibhav\nvaibhav")
print("vaibhav"+"k")
print(10*"vaibhav")


print("vaibhav", "k", "k", sep="--") #use of spereator instead of space
print("vaibhav",end='&&&&') #use of end
print("is",end='####')
print("good")
print(10,20,30,sep=':', end='***')
print(40,50,60,sep=':')

#string formating or replacement operator
a='vaibhav'
b=10000
print("hello {}, you salary is {}".format(a,b))
print("hello {0}, you salary is {1}".format(a,b)) #use of index of format
print("hello {n}, you salary is {s}".format(n=a,s=b))


#use of formatted string
name='vaibhav'
marks=[10,20,30]
print("hello %s, your marks list is %s" %(name,marks))

price=70.5678
print("price is {}".format(price))
print("price is %.2f" %price) #customising by formatted method
