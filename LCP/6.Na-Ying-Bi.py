class Solution:
    def minCount(self, coins: List[int]) -> int:
	# One-line Solution
	# return sum([coin//2+1 if coin%2 else coin//2 for coin in coins])

        ans = 0
        for coin in coins:
            if coin%2: ans += coin//2 + 1
            else: ans += coin//2
        return ans
