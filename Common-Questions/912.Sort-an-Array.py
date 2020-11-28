class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def division(nums, left, right):
            key = left
            while left < right:
                while left < right and nums[right] >= nums[key]:
                    right -= 1
                while left < right and nums[left] <= nums[key]:
                    left += 1
                nums[left], nums[right] = nums[right], nums[left]
            nums[key], nums[left] = nums[left], nums[key]
            return left

        def quicksort(nums, left, right):
            if left >= right: return
            mid = division(nums, left, right)
            quicksort(nums, mid+1, right)
            quicksort(nums, left, mid-1)

        if len(nums) <= 1: return nums
        quicksort(nums, 0, len(nums)-1)
        return nums
