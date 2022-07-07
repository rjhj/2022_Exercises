# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104



class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        position = 0
        while True:
            length = len(nums)
            middleposition = length//2
            if nums[middleposition] == target:
                return middleposition + position
            elif nums[middleposition] > target:
                if length == 1:
                    return middleposition + position
                nums = nums[0:middleposition]    
            elif nums[middleposition] < target:
                if length == 1:
                    return middleposition + position + 1
                nums = nums[middleposition:length]
                position += middleposition


class Test():
    testNums = [[1,3,5,6], [1,3,5,6], [1,3,5,6], [0], [1,2]]
    testTargets = [5, 2, 7, 9, 1]
    expectedResults = [2, 1, 4, 1, 0]

    def runTest(self, solution):
        for i in range(len(self.testNums)):
            result = solution.searchInsert(self.testNums[i], self.testTargets[i])
            print(f"Nums: {self.testNums[i]} Target: {self.testTargets[i]}", end = " ")
            print(f"Expected: {self.expectedResults[i]} Result = {result}")    


def main():
    solution = Solution()
    test = Test()
    test.runTest(solution)
    

if __name__ == "__main__":
    main()
