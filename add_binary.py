# Given two binary strings a and b,
# return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
 
# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros
# except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_int = self.bin_to_int(a) + self.bin_to_int(b)
        bin_s = str(bin(sum_int))
        return bin_s[2:]
    
    def bin_to_int(self, s):
        result = 0
        length = len(s)
        for i in range(0, length):
            if s[i] == "1":
                result += 2**(length - 1 - i)
        return result




        

#Testdata
a_list = ["11", "1010", "0"]
b_list = ["1", "1011", "11111"]
expected = ["100", "10101", "11111"]

solution = Solution()

#Tests
for i, v in enumerate(expected):
    result  = solution.addBinary(a_list[i], b_list[i])
    print(f"Expected: {v} Result: {result}")