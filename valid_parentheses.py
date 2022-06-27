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

    def valids(self, opened):
        opposites = {
           "(" : ")",
           "[" : "]",
           "{" : "}"
        }
        openBrackets = ["(", "[", "{"]
        correctClosing = []
        if opened:
            correctClosing = opposites[opened[-1]]
        return openBrackets + correctClosing


    def isValid(self, s: str) -> bool:

        openBrackets = ["(", "[", "{"]
        lengthOfTheString = len(s)
        if lengthOfTheString % 2 == 1:
            return False
        i = 0
        opened = []
        allowed = openBrackets
        while i < lengthOfTheString:
            validList = self.valids(opened)
            if s[i] not in validList:
                print(s[i])
                return False
            else:
                pass
            i += 1
        return True
        

solver = Solution()

# Test data
testStrings = ["()", "()[]{}", "(]", "{{{{", ")", "((([([])]))", "([)"]
expectedResults = [True, True, False, False, False, True, False]

i = 0
while (i < len(testStrings)):
    result = solver.isValid(testStrings[i])
    print("Expected result: " + str(expectedResults[i]) + " Result: " + str(result) + " Was the result correct? " + str(expectedResults[i] == result))
    i += 1