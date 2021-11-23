#pop(key)  key is must
d={1:2, 3:4, 5:6, 7:8, 9:10 }
print(d.pop(1)) #1 will be removed
print(d)

#pop(key,values) #value will be return
print(d.pop(2,"hello"))

#pop item will be removed random item gives in the tuplr form

print(d.popitem())

#clear removes all
d.clear()
print(d)

