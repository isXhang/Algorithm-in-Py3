class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1
        for i in range(0, len(nums)+1):
            if not hashmap.get(i, 0): return i
