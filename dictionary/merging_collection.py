#merging of list
l1=[1,2]
l2=[3,4]
l3=[*l1,*l2] #using * opr
print(l3)

#tuple mergin
t1=(10,20)
t2=(30,40)
t3=(*t1,*t2)
print(t3)

#set merging
s1={10,20}
s2={30,40}
s3={*s1,*s2}
print(s3)

#dict merging
d1={10:100,20:100}
d2={30:300,40:400}
d3={**d1,**d2}
print(d3)

