class Solution:
    def dailyTemperatures(self, T):
        if not T: return []
        res = [0] * len(T)
        stack = []
        for index, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                pop = stack.pop()
                res[pop] = index-pop
            stack.append(index)
        return res
