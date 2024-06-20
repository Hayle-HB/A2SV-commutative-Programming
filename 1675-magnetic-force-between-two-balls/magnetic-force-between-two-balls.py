class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def canPlaceBalls(min_dist):
            count = 1  # place the first ball in the first basket
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        left = 1
        right = position[-1] - position[0]
        
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
