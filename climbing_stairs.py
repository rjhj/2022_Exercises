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


from logging import StringTemplateStyle


class Solution:
    #I've decided to make this more challenging and print out all the possible variations.

    def node(self, n, str, level, strList):
        m = n
        str2 = str
        if n > 1:
            str += "2"
            n -= 2
            self.node(n, str, level, strList)
        if m > 0:
            str2 += "1"
            m -= 1
            self.node(m, str2, level, strList)
        if n == 0 and m != 1:
            strList.append(str)



    def climbStairs(self, n: int) -> int:
        str = ""
        strList = []
        solver.node(n, str, 0, strList)
        print(strList)

        return strList


solver = Solution()

#Test data
testData = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 5,
    5 : 8,
    6 : 13
    }

#Tests
for test, expected in testData.items():
    result = (solver.climbStairs(test))
    print(f"Test value: {test}, expected value: {expected}, solver gave: {len(result)}")
    print(f"All the possible variations: {result}")