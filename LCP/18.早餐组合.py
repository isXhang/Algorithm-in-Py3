class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        import bisect
        ans = 0
        drinks.sort()
        for i in staple:
            ans += bisect.bisect_right(drinks, x - i)
        return 1 if ans == 1000000008 else ans%1000000007

    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        ans = 0
        dp = [0 for _ in range(x+1)]
        for sta in staple:
            if sta < x:
                dp[sta] += 1

        for i in range(2, x):
            dp[i] += dp[i-1]
        for drink in drinks:
            money = x - drink
            if money <= 0:
                continue
            ans += dp[money]
        return 1 if ans == 1000000008 else ans%1000000007
