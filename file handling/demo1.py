#file handling
f=open('abc123.txt','x') #for x mode file should not be available already. 
print("name",f.name)
print("is closed",f.closed)
print("mode",f.mode)
print("redable",f.readable())
print("writable",f.writable())
f.close()
print("is closed",f.closed)