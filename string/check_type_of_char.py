s=input("enter a string ")
if s.isalnum():
    print("it is alpha numeric")
    if s.isalpha():
        print("all char are alphabetic")
        if s.islower():
            print("it is lower case ")
        elif s.istitle():
            print("it is title")
        else:
            print("it is upper case")
    if s.isdigit():
        print("it is digit")
elif s.isspace():
    print("it is a space char")
else:
    print("it is a non space special char")
