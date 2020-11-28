# Date: 2020-11-22
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # One-line Solution
        # return sorted(s) == sorted(t)

        t = list(t)
        for char in s:
            if char in t: t.remove(char)
            else: return False
        return len(t) == 0
