class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [sum(gain[:i+1]) for i in range(len(gain))]
        return max(prefix) if max(prefix) >= 0 else 0
        