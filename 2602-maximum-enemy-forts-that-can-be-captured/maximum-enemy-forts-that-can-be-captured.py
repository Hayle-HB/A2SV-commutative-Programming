class Solution:
    def captureForts(self, forts: List[int]) -> int:
        left, right = 0, len(forts)-1
        count = 0
        for i in range(len(forts)):
            if forts[i] == 1:
                left = i + 1
                while left < len(forts) and forts[left] == 0:
                    left += 1
                
                if left < len(forts) and forts[left] == -1:
                    count = max(count, left - i - 1)
                    i = left+1
        for i in range(len(forts)-1, -1, -1):
            if forts[i] == 1:
                right = i - 1
                while right >= 0 and forts[right] == 0:
                    right -= 1
                
                if right >= 0 and forts[right] == -1:
                    count = max(count, i - right - 1)
                    i = right - 1
        return count

       