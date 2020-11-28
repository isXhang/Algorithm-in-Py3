class Solution:
    def longestMountain(self, A: List[int]) -> int:
        length = len(A)
        res = 0
        for i in range(length-2):
            if A[i] < A[i+1] and A[i+1] > A[i+2]:
                j = i-1
                count = 3
                left = A[i]
                while j >= 0 and A[j] < left:
                    count += 1
                    left = A[j]
                    j -= 1

                j = i+3
                right = A[i+2]
                while j <= length-1 and A[j] < right:
                    count += 1
                    right = A[j]
                    j += 1
                res = max(res, count)
        return res

    def longestMountain(self, A: List[int]) -> int:
        length = len(A)
        up, down = [1]*length, [1]*length

        for index in range(1, length):
            if A[index] > A[index-1]:
                up[index] = up[index-1] + 1
            if A[length-index-1] > A[length-index]:
                down[length-index-1] = down[length-index] + 1

        res = 0
        for index in range(1, length-1):
            if A[index-1] < A[index] and A[index] > A[index+1]:
                res = max(res, up[index]+down[index]-1)
        return res

T = [[], [0], [2,2,2], [2,1,4,7,3,2,5], [1,2,1], [0,1,2,3,4,5,6,7,8,9]]
for t in T:
    print(Solution().longestMountain(t))
