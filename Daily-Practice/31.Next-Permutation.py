# Date: 2020-11-10
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        if sorted(nums, reverse=True) == nums:
            nums.sort()
            return

        length = len(nums)
        index = 0
        for i in range(length-2, -1, -1):
            if nums[i] >= nums[i+1]: continue
            index = i
            break
        for i in range(length-1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                left, right = index+1, length-1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left, right = left+1, right-1
                return
