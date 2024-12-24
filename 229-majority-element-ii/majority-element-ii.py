class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        answer = set()
        for num in nums:
            hash[num] += 1

            if hash[num] > len(nums) // 3 and num not in answer:
                answer.add(num)
        return list(answer)