class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            val = arr[i]
            for k in range(i + 1, n):
                val = xor(val, arr[k])
                if val == 0:
                    ans += k - i
        return ans