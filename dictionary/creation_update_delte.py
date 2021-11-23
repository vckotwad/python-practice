#empty dit
d={} # with curly braces

#using fuction
d1=dict() 

#using list of tuple or// tupe of tuples// or sest of tuple
l=[(100,200),(300,400),(500,600)] #only two element req
d2=dict(l)
print(d2)

#access
#membership opr 
if 500 in d2:
    print(d2[500])

#adding value, if present then update value
d2[10]=490
print(d2)

#del entty in dict if present
del(d2[10],d2[300]) # mutiple value can be
print(d2)