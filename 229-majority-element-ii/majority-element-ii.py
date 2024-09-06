class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return list(set(nums))
        ans = set()
        nums.sort()
        curr = 1
        [1, 2,2,3]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                curr += 1
            else:
                if curr > len(nums) // 3:
                    ans.add(nums[i-1])
                curr = 1
        
        if curr > len(nums) // 3:
            ans.add(nums[-1])
        return list(ans)