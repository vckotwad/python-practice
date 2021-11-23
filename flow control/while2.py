#sum of first n numbers using while loop
n=int(input("enter the number"))
a=0
sum=0
while a<=n:
    sum=sum+a
    a+=1
print(sum)

#using formula 
sum1=(n*(n+1))/2
print("sum of first {} numbers is:- {}".format(n, sum1))