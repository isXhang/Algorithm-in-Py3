class Solution:
    def isPalindrome(self, x: int) -> bool:
	# One-line Solution
        return str(x) == str(x)[::-1]
