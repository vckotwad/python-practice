item=[10,20,30,600,70,80,900]
new=[]
for i in  item:
    if i>500:
        print("{} value is greater than 500, insurance is required".format(i))
        continue
    new.append(i)

print("card with value less than 50o is",new)


