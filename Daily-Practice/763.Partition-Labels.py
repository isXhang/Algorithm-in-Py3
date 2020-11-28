class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {val:ind for ind, val in enumerate(S)}
        res = []

        num = 0
        j = dic[S[0]]
        for i in range(len(S)):
            num += 1
            if dic[S[i]] > j:
                j = dic[S[i]]
            if i == j:
                res.append(num)
                num = 0
        return res
