class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # One-line Solution
        # return list(set(range(1, len(nums)+1)) - set(nums)) if nums else []

        import collections
        hashmap = collections.defaultdict(int)
        for num in nums:
            hashmap[num] = 1
        ans = []
        for num in range(1, len(nums)+1):
            if hashmap[num] == 0: ans.append(num)
        return ans
