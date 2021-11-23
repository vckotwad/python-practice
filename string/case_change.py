s='Vaibhav how are you'
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.capitalize())

print("********************************")
#checking two string are equal or not 
a="   How  are you  "
b="how are You   "
if a.strip().lower().replace("  "," ")==b.strip().lower().replace("  "," "):
    print("both string are equal")
else:
    print("both strings are not equal")

print("********************************")
