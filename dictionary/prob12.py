#no of  times vowels occurs in string
word=input("enter a string")
d={}
v='aeiou'
for ch in word:
    if ch in v:
        d[ch]=d.get(ch,0)+1
print(d)
for k,v in d.items():
    print("{} occures {} times".format(k,v))