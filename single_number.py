# Given a non-empty array of integers nums, every element
# appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime
# complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

##### My first try. Works, but is slow.
# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         singles = []
#         for e in nums:
#             if e in singles:
#                 singles.remove(e)
#             else:
#                 singles.append(e)
#         return singles[0]

class Solution:
    #A better solution (not mine)
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

solution = Solution()

result = solution.singleNumber([3, 1, 2, 1, 2])

print(result)