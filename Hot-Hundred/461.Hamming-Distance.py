class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 0^1 = 1 1^0 = 1 0^0 = 0 1^1 = 0
        # a^b^c = a^c^b
        return bin(x ^ y).count("1")
