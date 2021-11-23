from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
result=(reduce(lambda x,y:x+y,range(1,101)))
print(result)