class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
	# One-line Solution
        # return (guess[0]==answer[0])+(guess[1]==answer[1])+(guess[2]==answer[2])
        # return [guess[i] - answer[i] for i in range(len(guess))].count(0)

        res = 0
        for i in range(3):
            if guess[i] == answer[i]:
                res += 1
        return res

