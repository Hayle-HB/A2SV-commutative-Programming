class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1}

        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            rem = curr % k if k != 0 else curr

            if rem in prefix:
                if right -  prefix[rem]  > 1:
                    return True
            if rem not in prefix:
                prefix[rem] = right
        return False