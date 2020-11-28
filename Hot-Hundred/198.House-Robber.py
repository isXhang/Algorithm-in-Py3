class Solution:
    def rob(self, nums: List[int]) -> int:
	# Space O(n)
        if not nums: return 0
        length = len(nums)
        dp = [0] * (length+1)
        dp[1] = nums[0]

        for i in range(2, length+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
	# Space O(1)
	prev, cur = 0, 0
        for i in nums:
           prev, cur = cur, max(prev+i, cur)
        return cur
