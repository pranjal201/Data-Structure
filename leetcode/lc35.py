# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

#  

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# for this problem we will be using binary search

# Time Complexity O(n/2) Binary Search
def searchInsert(input, target):
    low = 0
    high = len(input) -1
    while low <= high:
        mid = low + (high-low)//2
        if (target == input[mid]):
            return mid
        elif (target > input[mid]):
            low = mid + 1
        elif (target < input[mid]):
            high = mid -1

    return high+1
            


if __name__ == "__main__":
    input = [1,3,5,6]
    print(searchInsert(input,4) )
    
