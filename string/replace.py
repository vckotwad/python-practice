#replace(old,new)
s='abababababababa'
print(s)
print("id before",id(s))
s=s.replace('a','b')
print(s)
print("id before",id(s))

#remove spaces with replace operator

p='hello how are you'
p1=p.replace(' ','')
print('with count method no of spaces',p.count(' ')) 
print("without count method no of space",len(p)-len(p1))
print(p1)

