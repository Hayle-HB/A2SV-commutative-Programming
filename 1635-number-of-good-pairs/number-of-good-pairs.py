class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = defaultdict(int)

        count = 0
        for num in nums:
            if num in hash:
                count += hash[num]
            hash[num] += 1
        return count