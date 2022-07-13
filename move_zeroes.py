# Given an integer array nums, move all 0's to the end of
# it while maintaining the relative order of
# the non-zero elements.

# Note that you must do this in-place without making a copy
# of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]
 
# Constraints:
# 1 <= nums.length <= 10^4
# -231 <= nums[i] <= 2^31 - 1

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == 0:
                nums.append(nums.pop(i))
            i -= 1
        print(nums)


solution = Solution()
solution.moveZeroes([0,0])