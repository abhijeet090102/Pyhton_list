'''l = [5,1,5,3,5,9,6]
l.append(4)
# print(l)
# l.extend(4)
# print(l)
# l.extend([4,8])
# print(l)
# l.insert(4,8)
# print(l)
# l.index(4) item value and return the index no
# print(l.index(8)) 
# print(l.count(5))
# print(l.sort(reverse=True))
print(l.pop(5))
print(l.remove(5))
print(l)
del l[4]
print(l)
del l[0:4]
print(l)
l1 = [0]*5
print(l1)
l2 = [0 for i in range(4)]
print(l2)
print(l[2])
print(l[0:4])
l1 = len(l)
print("length",l1)
print(l[0: ])'''

'''2nd occurence in list and pop the value
if l[0] in l[1: ]:
    n = l[1: ].index(5)
    l.pop(n+1)
print(l)'''
'''WAP to delete duplicate item from the list from the end
if l[0] in l[1: ]:
    n = l[0: ].index(5)
    print(n)
    l.pop() wrong
print(l)'''

'''2d list of zero with size 3 x 3
l1 = [[0]*4]*3
print(l1)
l2 = [[0 for i in range(4)] for j in range(3)]
print(l2)
l1[0][0] = 1
print("without loop",l1)
l2[0][0] =1
print("loop",l2)'''

''' shallow copy of a to b
a = 5
b = a
if a is b:
    print("true")'''

'''deep copy
import copy
l = [1,2,5,7,[4,8]]
l1 = l
print (l1 is l)
print (l)
l2 = copy.deepcopy(l1)
print('deepcopy',l2)
l2[4][0] = 'am'
print('after changing',l2)'''

'''l1 = [[2,3,4],[1,5,6]]
l2 = [[1,5,6],[4,5,6]]
l3 = [[0 for k in range(3)]  for l in range(2)]
i = 0
j = 0
print(l3)
for i in range(2):
    for j in range(3):
        l3[i][j] = l2[i][j]+ l1[i][j]
print(l1)
print(l2)
print(l3)'''
st = "ma is my streangth of my goal "
print(st.split())  result is ['ma', 'is', 'my', 'streangth', 'of', 'my', 'goal']
print(st.split(' , ')) result is ['ma is my streangth of my goal ']
