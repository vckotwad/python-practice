#try except else finally '
from typing import final


f=None
try:
    f=open('abc.txt')
except:
    print("there is problem in locating file")
else:
    print("file open successfully ")
    print("content of the file is")
    print(f.read())
finally:
    if f is not None:
        f.close()