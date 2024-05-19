class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k
        pick_remain = k - numOnes - numZeros
        if pick_remain <= 0:
            return numOnes
        return numOnes - pick_remain