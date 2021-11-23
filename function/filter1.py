#filter out names start with k
h=["katrina","kareena","anushka","deepika","alia","kanisha"]
l=list(filter((lambda l:l[0]=="k"),h))
print(l)

#having name length as odd
odd=list(filter(lambda n:len(n)%2!=0, h))
print(odd)