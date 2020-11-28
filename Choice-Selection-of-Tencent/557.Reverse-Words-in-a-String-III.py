class Solution:
    def reverseWords(self, s: str) -> str:
        # One-line Solution
        # return ' '.join([string[::-1] for string in s.split(' ')])

        strings = s.split(' ')
        for index, string in enumerate(strings):
            strings[index] = string[::-1]
        return ' '.join(strings)
