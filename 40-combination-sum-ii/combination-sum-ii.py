class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(start, comb, total):
            if total == target:
                result.append(comb[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(i+1, comb, total + candidates[i])
                comb.pop()
        
        result = []

        backtrack(0, [], 0)
        return result        