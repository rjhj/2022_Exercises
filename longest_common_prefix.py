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
    def longestCommonPrefix(self, strs: list[str]) -> str:
        return ""




solver = Solution()

# Test data
testList = [["flower","flow","flight"], ["dog","racecar","car"]]
expectedResult = ["fl", ""]

i = 0
lenOfTestList = len(testList)
while i < lenOfTestList:
    result = solver.longestCommonPrefix(testList[i])
    print(result == expectedResult[i])
    i += 1