class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        if n == 3: return nums[0] + nums[1] + nums[-1]

        ans = float('inf')
        preAbs = float('inf')

        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                summary = nums[i]+nums[left]+nums[right]
                if abs(target-ans) > abs(target-summary):
                    preAbs = abs(target-summary)
                    ans = summary
                if summary > target:
                    right -= 1
                elif summary < target:
                    left += 1
                else:
                    return ans

        return ans
