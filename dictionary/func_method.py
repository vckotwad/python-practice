#len() , no of key value pair in dict
d1={1:'a',2:'b',3:'c'}
d2={4:'d',5:'e',6:'f'}
print(len(d1))

#d.get(key) gives no error if not presernt
print(d1.get(4,"hello")) #if not present we get our default return

#update add dict in d
d1.update(d2)
print(d1)

#keys() only keys will be printed
print(d1.keys())

#only values value()
print(d1.values())

#items() to get key value pair
print(d1.items()) #tuple is created


for k,v in d1.items():
    print(k,v)
