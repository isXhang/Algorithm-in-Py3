class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # One-line Solution
        return sorted(nums)[len(nums)//2]
