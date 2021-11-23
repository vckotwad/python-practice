'''
s= (lambda n:n*n) # ( lambda input argument : output expresson )
for i in range(1,11):
    print("the square of {} is {}".format(i,s(i)))

s=(lambda x,y:x+y) #sum of two numbers using lambda

for i in range(1,7):
    for j in range(1,7):
        print(s(i,j))
'''
bigger=(lambda a,b,c: a if a>b and a>c else b if b>c else c) #ternary operator
print(bigger(40,44,50))