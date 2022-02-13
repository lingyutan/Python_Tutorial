class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        res = 0
        for index in range(len(prices)-1):
            diff = prices[index+1] - prices[index]
            if diff > 0:
                res += diff
                print(res)

        return res
        
