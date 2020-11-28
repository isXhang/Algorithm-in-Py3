class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        a = b = -1
        length = len(cont)
        for i in range(length-1, -1, -1):
            if i == length-1: a, b = cont[-1], 1
            else:
                a, b = cont[i]*a+b, a
        return [a, b]
