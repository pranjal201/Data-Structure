'''------------------------------Problem #1 : Range Sum Queries using Prefix Sum------------------------------'''
#Description : We are given an Array of n integers, We are given q queries having indices l and r . We have to find out sum between the given range of indices.


#arr list of integers for applying operations
#operations number of operations
#indices contains the range to calculate the prefix sum

def prefix_sum(arr,operations,indices):
    sums = [0 for x in range(operations)]
    for i in range(0, operations):
        sums[i] = sum(arr[indices[i][0]:indices[i][1]+1])

    return sums
    






arr = [4,5,2,3,5]
operations = 3

indices = []
for i in range(0, operations):
    a = int(input("a="))
    b = int(input("b="))
    indices.append([a,b])

print(prefix_sum(arr,operations, indices)) 
