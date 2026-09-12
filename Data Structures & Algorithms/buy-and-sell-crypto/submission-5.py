class Solution:
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices)):
            buying = prices[i]
            profit = max(prices[i:]) - buying
            if profit > res:
                res = profit
        return res


            
        