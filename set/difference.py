#difference , present in s1 but not in s2
s1={1,2,3,4,5,6,7,8,9}
s2={1,2,3,4,5}
s3=s1.difference(s2)
print(s3)

#symmetric difference , except common elements
s4=s1.symmetric_difference(s2) #s3=s1^s2
print(s4)