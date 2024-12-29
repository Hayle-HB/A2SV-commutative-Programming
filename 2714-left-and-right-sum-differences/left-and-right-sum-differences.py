class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)

        answer = []
        curr = 0
        prev = 0
        for num in nums:
            curr += num           
            answer.append(abs(total-curr-prev))
            prev = curr

        return answer

        