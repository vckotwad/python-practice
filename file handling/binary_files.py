#handling binary files
f1=open('abc.png','rb')
data=f1.read()
print(type(data))
f2=open("xyz.png",'wb')
f2.write(data)
f1.close()
f2.close()