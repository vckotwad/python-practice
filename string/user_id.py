#user id not case sensitive password case sensitiv3e
u=input("enter user name ").lower()
p=input("enter password") #pass case sensitive
if u=='vaibhav' and p=='password':
    print("congratulation user authentiated")
else:
    print("user access deneid")