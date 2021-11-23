#reversed() inbuilt works
l=tuple(range(2,20))
t=tuple(reversed(l))
print(t)

#sortin using sorted() inbuilt function
s=tuple(sorted(t,reverse=True))
print(s)