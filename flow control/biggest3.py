a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))
d=int(input('enter fourth number'))

if a==b and a==c and a==d:
    print("all numbers are equal")
else:
     if a>b and a>c and a>d:
         print("{} is the largest number".format(a))
     elif b>c and b>d:
              print("{} is the largest number".format(b))
     elif c>d:
         print("{} is the largest number".format(c)) 
     else:
         print("{} is the largest number".format(d))   