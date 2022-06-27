"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

"""

# Returns the list of the two indices where the numbers add to the target.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        kierros = 1
        for n in nums:
            i = kierros
            for i in range(kierros, len(nums)):
                #print("Kierros: " + str(kierros) + " n: " + str(n) + " i: " + str(i) + " kierros -1, i: " + str(kierros-1) + ", " + str(i))
                #print (n + nums[i])
                if n + nums[i] == target:
                    return [kierros-1, i]
            kierros += 1
        return []
    
# Checks the results
def tarkistaja(knownResult, twoSumResult):
    if knownResult == twoSumResult:
        print("Hyvä! ", end='')
    else:
        print("Väärin! ", end='')
    print("Tuloksesi pitäisi olla " + str(knownResult) + " ja tuloksesi oli " + str(twoSumResult))


solver = Solution()

problems = [[2,7,11,15], [3, 2, 4], [3, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 2, 3]]
targets = [9, 6, 6, 19, 6]
knownresults = [[0, 1], [1, 2], [0, 1], [8, 9], [0, 2]]

i = 0
while i < len(targets):
    result = solver.twoSum(problems[i], targets[i])
    tarkistaja(knownresults[i], result)
    i += 1



# Success
# Details 
# Runtime: 4974 ms, faster than 19.48% of Python3 online submissions for Two Sum.
# Memory Usage: 14.8 MB, less than 99.44% of Python3 online submissions for Two Sum.