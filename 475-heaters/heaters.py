class Solution:
    def findRadius(self, houses, heaters):
        def binary_search(house, heaters):
            low = 0
            high = len(heaters) - 1
                                                                            
            min_left = float('-inf')  
            max_right = float('inf')  

            while low <= high:
                mid = (low + high) // 2  

                if house == heaters[mid]: 
                    return 0  
                elif house > heaters[mid]:
                    min_left = heaters[mid]  
                    low = mid + 1  
                else:
                    max_right = heaters[mid]  
                    high = mid - 1 
            
            return min(house - min_left, max_right - house)

        heaters.sort()

        max_radius = float('-inf')

        for house in houses:
            min_radius = binary_search(house, heaters)
            max_radius = max(max_radius, min_radius)

        return max_radius
