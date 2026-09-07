class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = float('inf')
        curr_profit = 0
        max_profit = 0
        for i in range(0, len(prices), 1):
            if prices[i] < buy_price:
                buy_price = prices[i]
            curr_profit = prices[i] - buy_price
            max_profit = max(max_profit, curr_profit)
        
        return max_profit
prices = [7,6,4,1,2,5,9]
s = Solution()
print(s.maxProfit(prices))