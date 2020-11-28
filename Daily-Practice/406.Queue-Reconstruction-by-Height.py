# Date: 2020-11-16
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        import functools
        def compare(x, y):
            if x[0] < y[0]:
                return -1
            elif x[0] > y[0]:
                return 1
            else:
                if x[1] < y[1]: return 1
                else: return -1
        people = sorted(people, key=functools.cmp_to_key(compare))

        res = [[] for _ in range(len(people))]
        index = list(range(len(people)))
        for item in people:
            res[index[item[1]]] = item
            del index[item[1]]
        return res

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
