class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        res = []
        if (numerator < 0) ^ (denominator < 0): res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        a, remained = divmod(numerator, denominator)
        res.append(str(a))
        if remained == 0: return ''.join(res)

        res.append('.')
        bracketsMap = {}
        while remained:
            if remained in bracketsMap:
                res.insert(bracketsMap[remained], '(')
                res.append(')')
                break

            bracketsMap[remained] = len(res)
            remained *= 10
            a, remained = divmod(remained, denominator)
            res.append(str(a))

        return ''.join(res)
