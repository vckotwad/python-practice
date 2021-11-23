#creating list with 1 to 10

#normal way
l=[]
for x in range(1,11):
    l.append(x)
print(l)

#list comprehension  way
lc=[x for x in range(1,21)]
print(lc)

#list comprehension with condition
l1=[x*x for x in range(1,11) if x%2==0]
print(l1)

#2 to the power of 1 to 5
l5=[2**x for x in range(1,6)]
print(l5)

#list from 1 to 100 divisible by 10
l6=[x for x in range(1,101) if x%10==0]
print(l6)

#element present in l7 but not in l8
l7=[10,20,30,40]
l8=[30,40,50,60]
l9=[x for x in l7 if x not in l8]
print(l9)

#list present in both l1 and l2
l10=[10,20,30,40]
l11=[30,40,50,60]
l12=[x for x in l10 if x in l11]
print(l12)

#create list only with first chat in elements of l
ls=['balaiah','nag','venki','chiru']
l15=[x[0] for x in ls]
print(l15)

#following string contains all words in alphabets
ls='the quick brown fox jumps over the lazy dog'
lz=ls.split()
print(lz)
l20=[[word.upper(),len(word)] for word in lz]
print(l20)
