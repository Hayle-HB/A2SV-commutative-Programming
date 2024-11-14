class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        answer = nums[0] + nums[1] + nums[2]

        for i, a in enumerate(nums):
            l = i + 1
            r = n - 1

            while l < r:
                curr = a + nums[l] + nums[r]
                if abs(target-curr) < abs(answer-target):
                    answer = curr
                if curr < target:
                    l += 1
                else:
                    r -= 1
        return answer
                
            