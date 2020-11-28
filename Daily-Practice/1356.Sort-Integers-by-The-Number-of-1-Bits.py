# Date: 2020-11-06
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # One-line Solution
        # return sorted(arr,key=lambda x:(bin(x).count('1'),x))
        res = [(num, bin(num).count('1')) for num in arr]
        import functools
        def compare(x, y):
            if x[1] < y[1]:
                return -1
            if x[1] > y[1]:
                return 1
            if x[1] == y[1]:
                if x[0] > y[0]: return 1
                else: return -1

        return [item[0] for item in sorted(res, key=functools.cmp_to_key(compare))]
