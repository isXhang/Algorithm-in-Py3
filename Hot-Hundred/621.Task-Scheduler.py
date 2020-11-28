class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import collections
        counter = collections.Counter(tasks)
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        max_time_task = counter[0][1]
        res = (max_time_task-1) * (n+1)

        for item in counter:
            if item[1] == max_time_task:
                res += 1

        return res if res >= len(tasks) else len(tasks)
