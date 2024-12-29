class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        curr = 0
        answer = [0] * len(queries)
        for i in range(len(nums)):
            curr += nums[i]

            for j in range(len(queries)):
                if curr <= queries[j]:
                    answer[j] = max(answer[j], i+1)
        return answer
            
        