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

#Function to check wether given string is an Anagram or 
# not
def isAnagram(s:str, t:str)->bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(0,len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for k in countS:
            if countS[k] != countT.get(k,0):
                return False
        return True

def groupAnagrams(strings:list[str])->list[list[str]]:
    # Setting the boundary condition for empty string and single stringelement
    length=len(strings)
    if length <= 1:
        return list(strings)

    finalResult = [[strings[0]]]
    i =1
    lock =0
    while i<length:
        for j in finalResult:
            lock = 0
            if isAnagram(strings[i],j[0]):
                j.append(strings[i])
                lock = 1
                break
        if lock == 0:
            finalResult.append([strings[i]])
        print(finalResult)
        i += 1
    return finalResult
    

if __name__ == '__main__':
    input =["eat","tea","tan","ate","nat","bat"] 
    print(groupAnagrams(input))