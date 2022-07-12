# Given an integer numRows, return the first numRows
# of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two
# numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]
 
# Constraints:
# 1 <= numRows <= 30


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        l = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        for i in range(2, numRows):
            temp_list = l[1].copy()
            for j in range(0, i-1):
                p = l[i-1][0+j] + l[i-1][1+j] 
                temp_list.insert(1,p)
            l.append(temp_list)
        return l

solution = Solution()

result = solution.generate(7)
print(result)
