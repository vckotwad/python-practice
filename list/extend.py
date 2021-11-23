l=list(range(1,10))
print(l)
l2=list(range(21,31))
l.extend(l2)
print(l)
s='vaibhav' #considered as seperate iterable elements
l.extend(s)
print(l)