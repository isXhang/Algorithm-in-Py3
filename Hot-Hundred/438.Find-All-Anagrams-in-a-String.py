class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Timeout
        sLen, pLen = len(s), len(p)
        res = []
        for index in range(sLen - pLen + 1):
            if sorted(s[index:index+pLen]) == sorted(p): res.append(index)
        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, sLen, pLen = [], len(s), len(p)
        if sLen < pLen: return res
        curList, pList = [0] * 26, [0] * 26
        for i in range(pLen):
            pList[ord(p[i]) - ord('a')] += 1
            curList[ord(s[i]) - ord('a')] += 1
        for i in range(sLen - pLen + 1):
            if pList == curList: res.append(i)
            if i + pLen < sLen:
                curList[ord(s[i]) - ord('a')] -= 1
                curList[ord(s[i+pLen]) - ord('a')] += 1
        return res
