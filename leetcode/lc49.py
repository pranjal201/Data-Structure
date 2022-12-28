# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

# using hashmap to reduce the time complexity from O(m.nlogn) to O(m.n.26)
import collections
def groupAnagrams(strings:list[str])->list[list[str]]:
   res = collections.defaultdict(list)

   for s in strings:
       count = [0] * 26 

       for c in s:
           count[ord(c) - ord("a")] +=1 
       res[tuple(count)].append(s)

   return res.values()


if __name__ == '__main__':
    input =["eat","tea","tan","ate","nat","bat"] 
    print(groupAnagrams(input))