'''-----------------------------oo-Problem #2 : Equilibrium index of an array------------------------------'''
#Description - Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at 
#higher indexes. We are given an Array of integers, We have to find out the first index i from left such that -


#first approach --- time complexity = O(N^2)
def equilibrium_01(arr):
    for i in range(0, len(arr)):
        if(sum(arr[0:i])==sum(arr[i+1:])):
            return i
    
    return -1


if __name__ == '__main__':

    arr = [-7, 1, 5, 2, -4, 3, 0]
    arr = [7, 2, 5, 2, 4, 3, 0]
    print(equilibrium_01(arr) )
