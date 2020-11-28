class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flag = -1
            x = -x
        else: flag = 1

        res = int(str(x)[::-1])
        res *= flag

        return res if res >= -2**31 and res <= 2**31-1 else 0
