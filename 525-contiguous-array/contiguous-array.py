class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {0:-1}

        maxLen = 0
        curr = 0


        for right in range(len(nums)):
            curr += 1 if nums[right] == 1 else -1

            if curr in prefix:
                maxLen = max(maxLen, right - prefix[curr])
            
            else:
                prefix[curr] = right
        return maxLen