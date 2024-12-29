class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        res = [0] * (101)

        for b, d in logs:
            res[b-1950] += 1
            res[d-1950] -= 1
        
        for i in range(1, len(res)):
            res[i] = res[i-1] + res[i]
        
        return res.index(max(res)) + 1950
        