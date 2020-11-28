class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0

        minus = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                minus = -1
            s = s[1:]

        res = ""
        for char in s:
            if char <= '9' and char >= '0':
                res += char
            else:
                break

        if res == "": return 0

        res = int(res) * minus
        if res < -2**31:
            return -2147483648
        elif res > 2**31-1:
            return 2147483647
        else:
            return res

