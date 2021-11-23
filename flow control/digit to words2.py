u19=['','one','two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine','ten','eleven','twelve','thirteen', 'fourteen','fifteen','sixteen','seventeen', 'eighteen','ninteen' ]
u10=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']


n=int(input('enter a number'))
if n==0:
    print("zero")
elif n==1000:
    print("one thousand")
elif n<=19:
    print(u19[n])
elif n<=99:
    print(u10[n//10],"",u19[n%10])
elif n<=999:
    print(u19[n//100],"hundred and",u10[(n%100)//10], u19[(n%100)%10] )
else:
    print("please enter number in the range of 1 to 1000")