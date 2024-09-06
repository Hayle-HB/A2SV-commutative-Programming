class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        ans = []
        for c in count:
            if count[c] > n // 3:
                for j in range(count[c]):
                    ans.append(c)

        return list(set(ans)) 