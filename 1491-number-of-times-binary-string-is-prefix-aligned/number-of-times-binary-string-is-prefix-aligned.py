class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        moves = 0
        right = 0

        for i in range(len(flips)):
            right = max(right, flips[i])
            if right == i + 1:
                moves += 1

        return moves
        