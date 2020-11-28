class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if num in res: res.remove(num)
            else: res.append(num)
        return res[0]

    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if res.get(num, 0) == 0: res[num] = 1
            else: res[num] += 1
        for key, val in list(res.items()):
            if val == 1: return key

    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
