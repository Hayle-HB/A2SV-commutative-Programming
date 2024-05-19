class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        count, minimum, answer = 0, math.inf, 0
        for n in nums:
            bar = n ^ k
            if n >= bar:
                minimum = min(minimum, n - bar)
                answer += n
            else:
                count ^= 1
                minimum = min(minimum, bar - n)
                answer += bar
        return answer - minimum * count