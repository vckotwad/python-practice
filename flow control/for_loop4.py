#print sum of number in the list
l=[]
sum=0

for x in  range(4):
    a=int(input("please enter number to added in list"))
    l.append(a)

for x in l:
    sum=sum+int(x)
print("the sum is ", sum)
