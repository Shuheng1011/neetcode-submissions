class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] < prices[buy]: 
                buy = sell

            else:
                maxPrice = max(maxPrice, (prices[sell] - prices[buy]))

            sell += 1

        return maxPrice
            

            