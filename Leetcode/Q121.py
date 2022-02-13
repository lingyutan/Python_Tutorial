class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]
        for price in prices:
            max_value = price
            if price < min_value:
                min_value = price
            else:
                max_profit = max(max_profit, max_value - min_value)

        return max_profit
        
