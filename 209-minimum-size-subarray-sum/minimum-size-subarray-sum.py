class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        minLen = float('inf')


        left = 0 
        

        for right in range(len(nums)):
            curr += nums[right]


            while curr >= target:
                minLen = min(minLen, right - left + 1)
                curr -= nums[left]
                left += 1
        return minLen if minLen != float('inf') else 0
