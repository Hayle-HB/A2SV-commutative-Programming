class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       hash = defaultdict(int)
       t = len(nums) // 2
       for num in nums:
        hash[num] += 1
        if hash[num] > t:
            return num

        