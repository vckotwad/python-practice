#packing
a,b,c,d=10,20,30,40
t=a,b,c,d
print(t)

#unpacking
a,b,c,d=t #no of values must be mathced
print(a,b,c,d)

#unpacking with *, remaining values assigned to b
a, *b=t
print(b)