class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 1:
            return False
        
        i = 0
        hash = set()
        while i < len(nums):
            if nums[i] in hash:
                return True
            hash.add(nums[i])
            if len(hash) > k:
                hash.remove(nums[i-k])
            i += 1
        return False
        