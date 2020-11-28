class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = [[]]
        for i in nums:
            res += [[i] + num for num in res]
        for i in res:
            i = sorted(i)
            if i not in ans:
                ans.append(i)
        return ans

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []
        if not nums: return []
        def recur(i, cur):
            res.append(cur)
            n = len(nums)
            for j in range(i, n):
                recur(j+1, cur + [nums[j]])
        recur(0, [])
        for i in res:
            i = sorted(i)
            if i not in ans:
                ans.append(i)
        return ans
