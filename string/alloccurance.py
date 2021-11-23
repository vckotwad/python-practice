s='abcabcabcabcabcabcabcabc'
i=0
k=0
dict={}
count=0
while i!=-1:
    i=s.find('abc',k)
    if i ==-1:
        break
    count= count+1
    print(count,i)

    k=k+3
print(dict)