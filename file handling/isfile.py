import os
k=(os.path.isfile('abc.txt')) #
if k== True:
    with open('abc.txt') as f:
        print(f.read())

else:
    print("file not found")