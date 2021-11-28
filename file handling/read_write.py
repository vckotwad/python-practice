#frst read data from file and then write
with open('abc.txt') as f:   #with block
   data=f.read()
   g=open('abcnew.txt','a')
   g.write(data)
