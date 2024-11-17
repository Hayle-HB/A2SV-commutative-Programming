class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_water = 0

        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            max_water = max(curr, max_water)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water

        