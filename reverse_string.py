# Write a function that reverses a string. The input string
# is given as an array of characters s.

# You must do this by modifying the input array in-place
# with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 
# Constraints:
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        last = len(s)-1
        for i in range(0,(last+1)//2):
            s[i], s[last-i] = s[last-i], s[i] 
        print(s)

solution = Solution()
solution.reverseString(["h","e","l","l","o"])
solution.reverseString(["1","2","3","4","5","6","7","8"])