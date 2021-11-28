#print file info


f=open("abc.txt")
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    wcount=wcount+len(line.split())
    ccount=ccount+len(line)

print("line count",lcount)
print("word count",wcount)
print("char count",ccount)



