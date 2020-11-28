class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # One-line Solution
        return list(set(nums1).intersection(set(nums2)))
