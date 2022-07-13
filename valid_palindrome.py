# A phrase is a palindrome if, after converting all uppercase
# letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and
# backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome,
# or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        ind1 = 0
        ind2 = len(s) - 1
        while ind2-ind1 > 0:
            match (s[ind1].isalnum(), s[ind2].isalnum()):
                case (True, True):
                    if s[ind1] != s[ind2]:
                        return False
                    else:
                        ind2 -= 1
                        ind1 += 1
                case (True, False):
                    ind2 -= 1
                case (False, True):
                    ind1 += 1
                case (False, False):
                    ind2 -= 1
                    ind1 += 1
        return True
        
solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result)


