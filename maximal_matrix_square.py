# Given an m x n binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return
# its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# Example 2:
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1

# Example 3:
# Input: matrix = [["0"]]
# Output: 0
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.

class Solution:

    def __init__(self):
        self.matrix = []
        self.row_len = 0
        self.col_len = 0


    def maximalSquare(self, matrix: list[list[str]]) -> int:
        self.matrix = matrix
        self.row_len = len(self.matrix)
        self.col_len = len(self.matrix[0])
        row = col = 0
        biggest_side_length = 0
        for row in range(0, self.row_len):
            for col in range(0, self.col_len):
                e = self.matrix[row][col]
                if e == "1":
                    biggest_side_length = max(biggest_side_length, 1)
                    found = True
                    while found:
                        trying_side_length = biggest_side_length + 1
                        found = self.it_fits(row, col, trying_side_length)
                        if found:
                            biggest_side_length = trying_side_length
        return biggest_side_length * biggest_side_length

    def it_fits(self, row, col, trying_side_length):
        if trying_side_length > self.col_len - col or trying_side_length > self.row_len - row:
            return False
        for i in range(row, trying_side_length+row):
            for j in range(col, trying_side_length+col):
                if self.matrix[i][j] == "0":
                    return False
        return True

solution = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","1"]]
result = solution.maximalSquare(matrix)
print(result)
