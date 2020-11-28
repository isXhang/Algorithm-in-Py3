class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Space O(1)
        length = len(nums)
        for i in range(length):
            while 0 < nums[i] <= length and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length+1

    def firstMissingPositive(self, nums: List[int]) -> int:
        # Space O(n)
        if not nums: return 1
        hashmap = {}
        for num in nums:
            if num > 0:
                hashmap[num] = 1
        for i in range(1, len(nums)+2):
            if not hashmap.get(i, 0): return i
