class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums: return []
        def recur(i, cur):
            res.append(cur)
            n = len(nums)
            for j in range(i, n):
                recur(j+1, cur + [nums[j]])
        recur(0, [])
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [[i] + num for num in res]
        return res
