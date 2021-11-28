#creating zip files

from zipfile import *
f=ZipFile('vaibhav.zip','w',ZIP_DEFLATED)
f.write('abc.txt')
print("file zip completed")