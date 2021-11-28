#working with directories
import os
print(os.getcwd()) #knowing current directories
os.mkdir("vaibhav13") #creating a directories in current directory
os.mkdir("vaibhav13/hello") #creating subdirectory
os.mkdir("c:\\vaibhav1234234") #creating file in other directories
os.makedirs("vaibhav1/vaibhav2/vaibhav3") #to create parent and child dir at the same time
os.rmdir("vaibhav1/vaibhav2/vaibhav3") #remove a dir, but only if its empty
os.removedirs("vaibhav1/vaibhav2") #remove from parent to child all directories