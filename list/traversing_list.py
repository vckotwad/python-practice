l=list("vaibhav")

#using for loop for accesssing
for i in l:
    print(i)
print(l)

#using for loop 
i=0
while i<len(l):

    print(l[i])
    i+=1

#print only even numbers
'''
for i in l:
    if i%2==0:
        print("even number is",i)
'''
#print element indexwise
i=0
ni=-(len(l))
for x in l:
    print("{} is present at +ve index {} and negative index {}".format(x,i,ni))
    i+=1
    ni=ni+1