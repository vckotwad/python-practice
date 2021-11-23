#aliasing affects both sets
s1={1,2,3}
s2=s1
s1.pop()
print(s2)

#cloning different object is created 
s3={1,2,3,4,5,6,7}
s4=s3.copy()
s3.pop()
print(s3)
print(s4)
