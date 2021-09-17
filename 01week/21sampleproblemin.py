'''--------------------------------------------Problem #3 : Largest Sum Subarray------------------------------'''
#Description : We are given an array of positive and negative integers. We have to find the subarray having maximum sum.
import sys
def Largest_subarray(arr):
    maximum = 0
    maximum_so_far = -sys.maxsize  #-9223372036854775807

    for i in range(0, len(arr)):
        maximum += arr[i]

        if(maximum_so_far < maximum):
            maximum_so_far = maximum

        if(maximum < 0):
            maximum = 0

    return maximum_so_far

if __name__ == '__main__':

    arr = [-3, -4, -4, -2, -4, -5]
    print(Largest_subarray(arr))
