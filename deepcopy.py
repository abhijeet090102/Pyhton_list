# deep copy in python
from copy import deepcopy
ma = [2,3,5,6,8]
am = deepcopy(ma)
print(am is ma)

'''# checking deep copy or not
ts = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # declearing 2d list
i= 0
st = [[i for k in range(4)  ]for j in range(4)]
# declaring 2d list using for loop this will reffer one object 
print(st is ts) # not same'''

'''from copy import deepcopy
l = [2,4,6,8]
l1 = deepcopy(l)
print(l1 is l)'''