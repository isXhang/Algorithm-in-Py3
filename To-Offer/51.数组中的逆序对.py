class Solution:
    def reversePairs(self, nums: List[int]) -> int:
	import bisect
        q = []
        for num in nums:
            i = bisect.bisect_left(q, -num)
            res += i
            q[i:i] = [-num]
        return res
