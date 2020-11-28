class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited: return num
            else: visited.add(num)

    def findDuplicate(self, nums: List[int]) -> int:
        # binary-sort
        nums.sort()
        cur = 0 ^ nums[0]
        pre = 0
        for index, num in enumerate(nums[1:]):
            cur ^= num
            if cur == pre: return num
            else: pre ^= nums[index]

