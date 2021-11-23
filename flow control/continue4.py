#divide 100 by  every number then return resul
l=[10,20,0,30,45,0,59,79]

for i in l:
    if i==0:
        print("100 cant be divided by 0")
        continue
    print("100/{} is {}".format(i,(100/i)))
