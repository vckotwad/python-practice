#write program to diffrent vowel presnt inside a word
w=set(input("enter a word").strip())
v=['a','e','i','o','u']
v1=set()
for x in w:
    if x in v:
        v1.add(x)

print(v1)

v2={'a','e','i','o','u'}
print(v2&w)

