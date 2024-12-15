class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total  = sum(beans)
        n = len(beans)
        ans = float('inf')


        for idx, val in enumerate(beans):
            ans = min(ans, total - val * (n - idx))
        
        return ans

        