class Solution:
    def calculate(self, s: str) -> int:
        # One-line Solution
        # return 1 << len(s) # <==> 2 ** len(s)

        x, y = 1, 0
        for char in s:
            if char == 'A':
                x = 2*x + y
            else:
                y = 2*y + x
        return x+y
