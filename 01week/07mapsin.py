'''
this is about chain maps or maps in python
using collection module 
just to understand the concept'''
from collections import ChainMap as maps

dict1 = {'day1': 'Mon', 'day2': 'Tue', 'day3': 'Wed'}
dict2 = {'day4':'Thu', 'day5': 'Fri', 'day6': 'Sat'}

redict =  maps(dict1, dict2)
print(redict.maps)

#output
'''[{'day1': 'Mon', 'day2': 'Tue', 'day3': 'Wed'}, {'day4': 'Thu', 'day5': 'Fri', 'day6': 'Sat'}]
'''
