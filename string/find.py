#find and rfind gives index
s='abcdefghibk'
print(s.find('b')) #if present
print(s.find("z")) #not present
print(s.rfind('b')) #search from right side
print(s.rfind("z")) #not present
print(s.find('b',4,16)) #search within given boundary