#to know the position of cursor
f=open('abc.txt')
print(f.tell()) #tells the position of cursor
f.read(10)
print(f.tell())