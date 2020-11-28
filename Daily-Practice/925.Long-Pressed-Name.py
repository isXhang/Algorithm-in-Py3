class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first, second = 0, 0
        m, n = len(name), len(typed)
        while second < n:
            if first < m and name[first] == typed[second]:
                first += 1; second += 1
            # elif second > 0 and typed[second] == name[first-1]:
            elif first > 0 and typed[second] == typed[second-1]:
                second += 1
            else:
                return False
        return first == m
