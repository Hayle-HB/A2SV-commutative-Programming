class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        max_r = 0
        heater = 0
        
        for i,house in enumerate(houses):
            while heater + 1 < len(heaters) and abs(heaters[heater] - house) >= abs(heaters[heater+1] - house):
                heater+=1
            max_r = max(max_r, abs(heaters[heater] - house))
        return max_r