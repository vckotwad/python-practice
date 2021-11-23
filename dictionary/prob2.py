#get each value in dict from key
d1={1:'a',2:'b',3:'c'}
d2={4:'d',5:'e',6:'f'}
r=eval(input("enter the key value"))
if r in d1:
    print("key is present")
else:
    print("key is not present")
        


#founding keys from values
r2=input("please enter the value")
for k in d1:
    if d1[k]==r2:
        print("key for the value", r2,"is", k)
        break
else:
    print("value not found in dict")


    
