class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        Sum =  0
        ans  = 0
        
        for g in gain:
            Sum += g

            ans = max(ans, Sum)
        return ans