class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        maxSum = nums[0]
        tmpSum = nums[0]
        for i in range(1, len(nums)):
            if tmpSum + nums[i] > nums[i]:
                tmpSum += nums[i]
                maxSum = max(maxSum, tmpSum)
            else:
                maxSum = max(maxSum, nums[i], tmpSum, tmpSum + nums[i])
                tmpSum = nums[i]
        return maxSum
