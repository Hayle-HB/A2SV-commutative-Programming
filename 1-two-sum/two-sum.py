class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for idx, num in enumerate(nums):
            comp = target - num

            if comp in hash:
                return [idx, hash[comp]]
            else:
                hash[num]  = idx
        return []