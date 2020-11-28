class Solution:
    def numTrees(self, n: int) -> int:
	# One-line Solution
	# Catalan Number
	# G(n)=G(0)*G(n−1)+G(1)*(n−2)+...+G(n−1)*G(0)
	# ==> (2n)! / ((n+1)! * n!)
	return math.factorial(2*n) // (math.factorial(n+1) * math.factorial(n))

    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

    visited = dict()
    def numTrees(self, n: int) -> int:
        if n in self.visited: return self.visited[n]
        if n <= 1: return 1
        res = 0
        for i in range(1, n+1):
            res += self.numTrees(i-1) * self.numTrees(n-i)
        self.visited[n] = res
        return res
