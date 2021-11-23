#check if number is prime or not
n=int(input("please enter a number"))
factors=[]
if n<=1:
    print("this is not prime number")
else:
     for i in range(1,n+1):
         if n%i==0:
             factors.append(i)
     print("the factors of {} are".format(n),factors)
     if factors[1]==n: #if in list there are only two factors then prime number
         print("{} is prime number".format(n))
     else:
         print("{} is not prime number".format(n))


