class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # Timeout
        n = len(a)
        res = [1] * n
        for i in range(n):
            for j in range(i-1, -1, -1):
                res[i] *= a[j]
            for j in range(i+1, n):
                res[i] *= a[j]
        return res

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        b, cur = [1] * n, 1
        for i in range(1, n):
            b[i] = b[i-1] * a[i-1]
        for i in range(n-2, -1, -1):
            cur *= a[i+1]
            b[i] *= cur
        return b
