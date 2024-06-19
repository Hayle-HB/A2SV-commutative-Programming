class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        pair = []

        n = len(weights)

        if n == k:
            return 0
        
        for i in range(n-1):
            pair.append(weights[i] + weights[i+1])
        pair.sort()

        res = 0
        for i in range(k - 1):
            res += pair[n - 2 - i] - pair[i]
            
        return res

        