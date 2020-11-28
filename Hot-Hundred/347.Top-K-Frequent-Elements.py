class Solution:
    def topKFrequent(self, nums, k):
        # One-line Solution
        # return [_[0] for _ in Counter(nums).most_common(k)]

        import heapq
        import collections
        counter = collections.Counter(nums)

        heap = []
        for i in counter:
            heapq.heappush(heap, (-counter[i], i))
        return [ heapq.heappop(heap)[1] for _ in range(k) ]

print(Solution().topKFrequent([1,1,1,3,2,2],2))
