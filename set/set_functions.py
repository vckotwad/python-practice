#len() method
s={10,20,34,450,230}
print(s)
print(len(s)) 

#add method
s.add(90)
print(s)
s.add(60)
print(s)

#update() add mutiple items must be iterable
l=[100,200,3000,4000]
k='vaibhav'
s.update(l,k)
print(s)

#removing item if item present
s.remove('v')
print(s)
 
#discard removes item if present otherwies no error 
s.discard('z') #no error if not present
print(s)

#pop removes random elements
z={10,20,30,405,505}
a=z.pop()
print(z)
print(a)
z.clear()
print(z)