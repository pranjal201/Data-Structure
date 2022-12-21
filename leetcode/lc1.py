# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# # Time Complexity O(n) and space complexity O(n)


def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0,len(nums)):
            temp = target-nums[i]
            if  temp in hashmap.keys():
                return [i, hashmap[temp]]
            hashmap[nums[i]] = i
