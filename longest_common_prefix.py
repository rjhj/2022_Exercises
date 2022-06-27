# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:

    def findShortestWord(self, strs):
        shortestLength = len(strs[0])
        shortestWordIndex = 0
        numberOfStrings = len(strs)
        i = 1
        while i < numberOfStrings:
            if shortestLength > len(strs[i]):
                shortestLength = len(strs[i])
                shortestWordIndex = i
            i += 1
        return shortestWordIndex
          
    def longestCommonPrefix(self, strs: list[str]) -> str:

        print(self.findShortestWord(strs))
        for s in strs:
            pass

            
        return ""




solver = Solution()

# Test data
testList = [["flower","flow","flight"], ["dog","racecar","car"], ["milk","milk","m"]]
expectedResult = ["fl", "", "m"]

i = 0
lenOfTestList = len(testList)
while i < lenOfTestList:
    result = solver.longestCommonPrefix(testList[i])
    print(result == expectedResult[i])
    i += 1