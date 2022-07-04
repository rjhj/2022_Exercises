# Implement strStr().
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string?
# This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
 
# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)    

solver = Solution()

#Testdata
haystacks = ["hello", "aaaaa", "jee"]
needles = ["ll", "bba", ""]
expectedResults = [2, -1, 0]

#Tests
for i in range(len(haystacks)):
    result = solver.strStr(haystacks[i], needles[i])
    print(f"Expected: {expectedResults[i]}, result: {result}")