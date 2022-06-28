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
        correctClosing = []
        if opened:
            correctClosing = opposites[opened[-1]]
        return openBrackets + list(correctClosing)


    def isValid(self, s: str) -> bool:
        lengthOfTheString = len(s)
        if lengthOfTheString % 2 == 1:
            return False
        i = 0
        opened = []
        while i < lengthOfTheString:
            validList = self.valids(opened)
            if s[i] not in validList:
                return False
            else:
                # Closing parentheses was found so previous open one can be removed 
                if s[i] not in openBrackets:
                    opened.pop()
                else:
                    opened.append(s[i])
            i += 1
        # All opened parentheses must be closed, so list must be empty
        if not opened:
            return True
        else:
            return False


openBrackets = ["(", "[", "{"]

solver = Solution()

# Test data
testStrings = ["()", "()[]{}", "(]", "{{{{", ")", "((([([])])))", "([)"]
expectedResults = [True, True, False, False, False, True, False]



i = 0
while (i < len(testStrings)):
    result = solver.isValid(testStrings[i])
    print(f'Expected result: {expectedResults[i]}, Result: {result}')
    i += 1


# Success
# Runtime: 45 ms, faster than 55.97% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 23.64% of Python3 online submissions for Valid Parentheses.