l = [4,5,6,7,8,4]
#l = input('Enter any no')

if l[0] in l[1:]:
    print('occured in other than 0')
else:
    print('Not Occured')
print(l)
l.append(20)
print(l)
# adding list value in last using extend 
l.extend([40,4,6,8])
print(l)
# pop will remove the index value
l.pop(4)
print(l)
# remove will remove the value occur in first time
l.remove(40)
print(l)
# this pop will remove the index value
l.pop(3)
print(l)

am = [0]*5
# create a list of five zero
print('\n',am)
st = [0 for i in range(5)]
print(st)
del l[2]
print(l)

'''' creating a 2d list of zero(0)'''
ma = [[0]*3]*3
print(ma)
'''creating a 2d list of zero(0) using for loop'''
ts = [[0 for i in range(3)]for i in range(3)]
print (ts)
