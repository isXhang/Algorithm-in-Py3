class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        import collections
        counter = collections.Counter(arr)
        res = list(counter.values())
        return sorted(res) == sorted(set(res))
