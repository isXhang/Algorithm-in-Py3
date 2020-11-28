class Solution(object):
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        n = len(prices)

        def dfs(index, status):
            if index == n: return 0
            a, b, c = 0, 0, 0
            a = dfs(index+1, status)
            if status:
                b = dfs(index+1, 0) + prices[index] - 2
            else:
                c = dfs(index+1, 1) - prices[index]
            return max(a, b, c)
        return dfs(0, 0)

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        hashmap = {}
        n = len(prices)

        def dfs(index, status):
            if index == n: return 0
            if (index, status) in hashmap: return hashmap[(index, status)]
            a, b, c = 0, 0, 0
            a = dfs(index+1, status)
            if status:
                b = dfs(index+1, 0) + prices[index] - 2
            else:
                c = dfs(index+1, 1) - prices[index]
            hashmap[(index, status)] = max(a, b, c)
            return max(a, b, c)
        return dfs(0, 0)

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0; dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]

print(Solution().maxProfit([1,2,3,4,5,2,8,4,9], 2))
