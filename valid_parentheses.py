# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        return True
        

solver = Solution()

# Test data
testStrings = ["()", "()[]{}", "(]", "{{{{", ")", "((([([])]))"]
expectedResults = [True, True, False, False, False, True]

i = 0
while (i < len(testStrings)):
    result = solver.isValid(testStrings[i])
    print("Expected result: " + str(expectedResults[i]) + " Result: " + str(result) + " Was the result correct? " + str(expectedResults[i] == result))
    i += 1