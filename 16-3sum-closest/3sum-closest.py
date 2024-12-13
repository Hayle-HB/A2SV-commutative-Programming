class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        answer = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if abs(curr - target) < abs(answer-target):
                    answer = curr
                if curr < target:
                    left += 1  
                else:
                    right -= 1
        return answer


        