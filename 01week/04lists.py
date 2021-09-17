from array import *

arr1 = array('i',[a for a in range(1,10,2)])
arr2 = array('i',[a for a in range(2,20,2)])
arr3 = array('i',[a for a in range(3,30,2)])
arr4 = array('i',[a for a in range(4,40,2)])

lists = []
lists.append(arr1)
lists.append(arr2)
lists.append(arr3)
lists.append(arr4)

for i in lists:
    for j in i:
        print(j, end=' ')
    print()

