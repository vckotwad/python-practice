#no of occurance of each letter in string
word=input("please enter a str")
l=[]
d=dict()
for x in word:
    if x not in l:
            l.append(x)
            d=word.count(x)
            print(x,"is present",d,"times") 

for ch in word:
    d[ch]=d.get(ch,0) + 1
print(d)
    



