'''
This is about understanding tuples 
in python
'''

tup = ()
print(tup)
tup = list(tup)
print(tup)
tup.append(5)
tup.append(5)
tup.append(4)
tup = tuple(tup)
tup[1] = 0
print(tup[1])
