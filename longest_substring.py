# Given a string s, find the length of the longest substring
# without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer = 0
        temp_longest = 0
        longest = 0
        i = 0
        while i < len(s):
            if s[i] in s[pointer:i]:
                pointer = s[pointer:i].find(s[i]) + len(s[0:pointer]) + 1
                if temp_longest > longest:
                    longest = temp_longest
                temp_longest = 0
                i = pointer+1
            else:
                i += 1
            temp_longest += 1
        if temp_longest > longest:
            longest = temp_longest
        return longest


solution = Solution()

tests = ["pwwkew", "abcabcbb", "", "y", "ba", "bbbbb", "abcabcbb"]
expected = [3, 3, 0, 1, 2, 1, 3]

for i, v in enumerate(expected):
    result = solution.lengthOfLongestSubstring(tests[i])
    print(f"ExpectedResult: {v} Result: {result}")
