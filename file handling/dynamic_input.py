#dynamic input 
name=input("enter the name of file you want write")
data=input("what data you want write")
f=open(name,'w')
f.write(data)