#seek() for moving cursor
f=open("abc.txt")
f.seek(3) #cursor moved from fist three characters
print(f.readline()) #remaining line is printed