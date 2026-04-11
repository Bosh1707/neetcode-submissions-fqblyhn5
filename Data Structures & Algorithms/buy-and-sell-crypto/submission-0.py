class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = 0
        minimum = 1000
        for n in prices:
            if n < minimum:
                minimum = n
            maximum_profit = max(maximum_profit, n - minimum)
        return maximum_profit 