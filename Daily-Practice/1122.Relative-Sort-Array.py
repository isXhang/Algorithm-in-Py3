# Date: 2020-11-14
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            count = arr1.count(i)
            res.extend([i] * count)
            for _ in range(count):
                arr1.remove(i)
        res.extend(sorted(arr1))
        return res

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 += sorted(set(arr1) - set(arr2))
        arr1.sort(key=lambda x: arr2.index(x)) # key=arr2.index
        return arr1
