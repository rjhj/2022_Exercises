# Given a string s consisting of words and spaces,
# return the length of the last word in the string.

# A word is a maximal substring consisting
#  of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 
# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s)
        while True:
            if s[last-1].isspace():
                last -= 1
            else:
                break
        first = last
        while first > 0:
            if not s[first-1].isspace():
                first -= 1
            else:
                return last - first
        return last

solution = Solution()

#Test data
testList = ["a", "aa", "Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]
expectedResults = [1, 2, 5, 4, 6]

#Tests
for i, test in enumerate(testList):
    result = solution.lengthOfLastWord(test)
    print(f"Expected: {expectedResults[i]} Result: {result}")
