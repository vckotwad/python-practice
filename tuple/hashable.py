#hashable or not
import collections
from typing import Collection, Hashable

import collections
s=set(range(21,30))
l=[1,2,3,4,4,]
t=(14,325,53,63,)
#print(isinstance(l,collections(Hashable=True)))
#print(isinstance(t,collections(Hashable)))
s.add(t)
print(s)
#s.add(l) #list is unhashable so cant be added
#print(s)