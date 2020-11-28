class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if max([x[1] for x in clips]) < T: return -1

        import collections
        dic = collections.defaultdict(int)
        for clip in clips:
            if clip[1] > dic[clip[0]]:
                dic[clip[0]] = clip[1]
        if 0 not in dic: return -1

        res = [(0, dic[0])]
        stack = [dic[0]]
        board = 1
        pre = int()
        while stack and stack[-1] < T and stack[-1] != pre:
            i = stack.pop(0)
            res.append((i, dic[i]))
            for j in range(board, i+1):
                if dic[j] > res[-1][1]:
                    res.pop()
                    res.append((j, dic[j]))
            if res[-1][1] <= res[-1][0]: res.pop()
            board = i+1
            stack.append(res[-1][1])
            pre = i

        return len(res) if res[-1][1] >= T else -1

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [101] * (T+1)
        dp[0] = 0

        for i in range(1, T+1):
            for clip in clips:
                if clip[0] < i <= clip[1]:
                    dp[i] = min(dp[i], dp[clip[0]]+1)

        return dp[T] if dp[T] != 101 else -1
