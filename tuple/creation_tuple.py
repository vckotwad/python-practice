#creation of tuple
t=10,10,130,40 #even without parenthesis
print(type(t))

#t[0]=50 # cant not be changed
#use where content cant be changing
print(t[-1]) #type error

#single value in coma gives int type
t1=(10)
print(type(t1))


#empty tuple
s=() 
print(type(s))


#single valued need coma,end with comma accepted
t=(10,) #without parenthesis treated as tuple
print(type(t))

#by using tuple() function
#using range
tf=tuple(range(1,11,3))
print(tf)

#using list
l=[10,20,30,40]
tf1=tuple(l)
print(tf1)

#using string
v='vaibhav'
tf2=tuple(v)
print(tf2)

#by dynamic input
p=eval(input("enter tuple values"))
print(type(p))