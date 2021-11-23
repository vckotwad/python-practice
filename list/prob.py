#add num divisible by 10 from 1 to 100
l=[]
for x in range(1,101):
    if x%10==0:
        l.append(x)

print(l)
