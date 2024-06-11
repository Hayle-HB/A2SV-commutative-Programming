class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order_map = {value: index for index, value in enumerate(arr2)}
        
        def custom_key(x):
            return (order_map.get(x, len(arr2) + x), x)
        
        sorted_arr1 = sorted(arr1, key=custom_key)
        
        return sorted_arr1