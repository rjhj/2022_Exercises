# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 
# Constraints:
# 1 <= n <= 45

##############################################
##                MY SOLUTION               ## 
##############################################
# To solved this I figured out the pattern in results:
# 2 total 2:                1 + 1
# 3 total 3:		        2 + 1
# 4 total 5:           1  + 3 + 1
# 5 total 8:           3  + 4 + 1
# 6 total 13:     1  + 6  + 5 + 1
# 7 total 21:     4  + 10 + 6 + 1
# 8 total 34: 1 + 10 + 15 + 7 + 1
#
# Combination of these permutations is the answer.
#
# For each permutation using n! / n2! * n1!
# where n = total number of elements
# n2 = number of twos, n1 = number of ones
# For example,
# 8 total 34: 1 + 10 + 15 + 7 + 1
# n           4    5    6   7   8
# n2          4    3    2   1   0
# n1          0    2    4   6   8
#
# To get 15 we calculate:
# math.factorial(6)/(math.factorial(2)*math.factorial(4))
# although I won't import math here.

class Solution:
    
    def factorial(self, n):
        product = 1
        for i in range(1, n+1):
            product *= i
        return product


    def permutations(self, n, n2, n1):
        return self.factorial(n) / (self.factorial(n2) * self.factorial(n1))


    def climbStairs(self, n: int) -> int:
        sum = 0
        end = n
        if n % 2 == 0:
            #all twos
            n2 = int(n/2)
            n = n2
            n1 = 0
        else:
            #all twos, single one
            n2 = int(n/2)
            n = n2 + 1
            n1 = 1
        start = n2
        for i in range(start, end + 1):
            sum += self.permutations(n, n2, n1)
            n += 1
            n2 -= 1
            n1 += 2
        return int(sum)
        
solver = Solution()

#Test data
testData = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 5,
    5 : 8,
    6 : 13,
    7 : 21,
    8 : 34,
    9 : 55,
    10 : 89
    }

#Tests
for test, expected in testData.items():
    result = (solver.climbStairs(test))
    print(f"Test value: {test}, expected value: {expected}, solver gave: {result}")


# Success 
# Runtime: 36 ms, faster than 78.48% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 56.80% of Python3 online submissions for Climbing Stairs.