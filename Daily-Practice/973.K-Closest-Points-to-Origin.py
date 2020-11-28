# Date: 2020-11-09
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import math
        import heapq
        pointsLen = []
        for point in points:
            pointLen = math.sqrt(point[0]*point[0] + point[1]*point[1])
            heapq.heappush(pointsLen, (pointLen, point))
        res = []
        for _ in range(K):
            res.append(heapq.heappop(pointsLen)[1])
        return res
