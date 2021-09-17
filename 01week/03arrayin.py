'''
This program is about array's in  python
date- 11/9/21
'''
from array import *

arr = array('i', [1,2,3,4] )
print(arr)

arr.append(8)
arr.insert(3,10)
for i in arr:
    print(i, end=" ")


char_arr = array('u', ['a', 'b','c'])
print(char_arr)

for i in char_arr:
    print(i, end=" ")
print()

newarr = array(arr.typecode, [a for a in range(100)])

for i in newarr:
    print(i, end=" ")
print()

print(newarr.buffer_info())
