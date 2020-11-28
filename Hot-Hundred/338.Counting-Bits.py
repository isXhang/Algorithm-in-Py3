class Solution:
    def countBits(self, num):
        # One-line Solution
        # return [bin(i).count('1') for i in range(num+1)]

        res = []
        for i in range(num+1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            res.append(count)

        return res
