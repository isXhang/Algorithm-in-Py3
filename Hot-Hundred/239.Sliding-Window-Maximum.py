class Solution:
    def maxSlidingWindow(self, nums, k):
        # Timeout
        # res = []
        # for i in range(k-1, len(nums)):
        #     res.append(max(nums[i-k+1:i+1]))
        # return res

        res = []
        import collections
        deque = collections.deque()

        for index, num in enumerate(nums):
            if deque and deque[0] <= index-k:
                deque.popleft()
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(index)
            if index >= k-1:
                res.append(nums[deque[0]])

        return res

print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
