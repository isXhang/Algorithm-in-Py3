class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price-minPrice)
        return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        minPrice = prices[0]
        dp = [0]*len(prices)

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minPrice)
        return max(dp)
