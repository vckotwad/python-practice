#generator will give one value at a time instead of storing all value at once like in traditional colleciton 
def value(n):
    i=1
    while i<=n:
        yield i
        i+=1

g=value(100000000)
for x in g: #for each value in g print the values
    print(x)