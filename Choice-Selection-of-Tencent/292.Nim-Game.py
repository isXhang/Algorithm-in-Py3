class Solution:
    def canWinNim(self, n: int) -> bool:
        # Nim游戏, 只要数字总数n, 能取得的最小值a和能取得的最大值b加起来的和c. 有如下关系.
        # n % c == 0 先手必输, 否则, 先手只要抢到余数就必胜。
        # One-line Solution
        return n%4 != 0

    def canWinNim(self, n: int) -> bool:
        # Out of Memory
        if n <= 3: return True
        dp = [False] * (n+1)
        dp[1], dp[2], dp[3] = True, True, True

        for i in range(4, n+1):
            if not dp[i-3] or not dp[i-2] or not dp[i-1]:
                dp[i] = True
        return dp[n]

    def canWinNim(self, n: int) -> bool:
        # Timeout
        if n <= 3: return True
        dp1, dp2, dp3 = True, True, True
        for i in range(4, n+1):
            if not dp1 or not dp2 or not dp3:
                dp = True
            else: dp = False
            dp1, dp2, dp3 = dp2, dp3, dp
        return dp
