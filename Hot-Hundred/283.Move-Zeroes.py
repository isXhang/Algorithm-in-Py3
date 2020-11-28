class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for _ in range(count):
            nums.remove(0)
            nums.append(0)

    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
