class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        length = len(nums)
        if length == 0: return 0

        for _ in range(length):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        return i+1
