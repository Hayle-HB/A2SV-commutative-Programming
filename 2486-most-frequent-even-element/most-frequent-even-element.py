class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(nums)

        for c in count:
            print(c, ' : ', count[c])

        ans = -1
        _max = 0
        for c in count:
            if c % 2 == 0:
                if count[c] > _max:
                    _max = count[c]
                    ans = c
        for c in count:
            if count[c]  == _max  and c % 2 == 0:
                ans = min(ans, c)
        return ans