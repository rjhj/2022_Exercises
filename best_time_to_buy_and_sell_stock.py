# You are given an array prices where prices[i] is the price
# of a given stock on the ith day.

# You want to maximize your profit by choosing a single day
# to buy one stock and choosing a different day in
# the future to sell that stock.

# Return the maximum profit you can achieve from this
# transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5
# (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1
# is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done
# and the max profit = 0.
 
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

############# MY FIRST TRY##################
# 
#     def maxProfit(self, prices: list[int]) -> int:
#         profit = 0
#         smallest = prices[0]
#         for e in prices:
#             if e < smallest:
#                smallest = e
#             else:
#                 if e - smallest > profit:
#                     profit = e - smallest
#         return profit
###########################################


class Solution:
    # MY SECOND TRY
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        smallest = prices[0]
        for e in prices:
            smallest = min(e, smallest)
            temp_profit = e - smallest
            profit = max(profit, temp_profit)
        return profit


def main():
    solution = Solution()
    #Testdata
    prices = [[7,1,5,3,6,4], [7,6,4,3,1], [1,2], [2,2,2,4,3]]
    expt_profits = [5, 0, 1, 2]

    #Tests
    for i, v in enumerate(expt_profits):
        result = solution.maxProfit(prices[i])
        print(f"Expected: {v} Result: {result}")   



if __name__ == "__main__":
    main()