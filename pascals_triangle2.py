# Given an integer rowIndex, return the rowIndexth (0-indexed)
# row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of
# the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
 
# Constraints:
# 0 <= rowIndex <= 33

class Solution:
    def factorial(self, n):
        if n == 0:
            return 1
        sum = 1
        for i in range(1, n+1):
            sum *= i
        return sum

    def n_choose_k(self, n, k):
        return int(self.factorial(n) / (self.factorial(k)*
        self.factorial(n-k)))

    def getRow(self, rowIndex: int) -> list[int]:
        result_list = []
        for i in range(rowIndex+1):
            result_list.append(self.n_choose_k(rowIndex, i))
        return result_list



solution = Solution()
print(solution.getRow(4))