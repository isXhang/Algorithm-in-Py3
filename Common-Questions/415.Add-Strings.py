class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2): num1, num2 = num2, num1
        num1, num2 = num1[::-1], num2[::-1]

	# To handle the final carry, make len(num1) == len(num2)
        for _ in range(len(num2)-len(num1)):
            num1 += "0"

        res = str()
        counter = 0
        ord0 = ord('0')
        for i in range(len(num1)):
            val = ord(num1[i]) - ord0 + ord(num2[i]) - ord0 + counter
            if val >= 10:
                counter = 1
                val -= 10
            else: counter = 0
            res += str(val)
        return (res + "1")[::-1] if counter else res[::-1]

    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2): num1, num2 = num2, num1
        num1, num2 = num1[::-1], num2[::-1]
        res = str()
        counter = 0
        ord0 = ord('0')
        for i in range(len(num1)):
            val = ord(num1[i]) - ord0 + ord(num2[i]) - ord0 + counter
            if val >= 10:
                counter = 1
                val -= 10
            else: counter = 0
            res += str(val)

	# To handle the overflow carry, should not be that complex
        if counter:
            if len(num1) == len(num2): return "1" + num2[i+1:][::-1] + res[::-1]
            else:
                for i in range(i+1, len(num2)+1):
                    if i == len(num2):
                        if counter == 1:
                            res += "1"
                        break
                    val = ord(num2[i]) - ord0 + counter
                    if val == 10:
                        counter = 1
                        val -= 10
                    else: counter = 0
                    res += str(val)
                return res[::-1]
        else:
            return num2[i+1:][::-1] + res[::-1]


    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

	# The optimized solution of Way1
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
