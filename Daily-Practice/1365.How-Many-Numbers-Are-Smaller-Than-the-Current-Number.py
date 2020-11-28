class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            if value in hashmap:
                hashmap[value].extend([index])
            else:
                hashmap[value] = [index]

        res = [0] * len(nums)
        nums.sort(reverse=True)
        for index, num in enumerate(nums):
            if num == nums[index-1]: continue
            numIndices = hashmap[num]
            for numIndex in numIndices:
                res.pop(numIndex)
                res.insert(numIndex, nums[::-1].index(num))

        return res

print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
