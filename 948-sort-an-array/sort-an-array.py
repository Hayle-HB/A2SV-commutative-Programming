class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)
        
        def merge(left, right):
            l, r = 0, 0
            sorted_arr = []

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    sorted_arr.append(left[l])
                    l += 1
                else:
                    sorted_arr.append(right[r])
                    r += 1
            sorted_arr.extend(left[l:])
            sorted_arr.extend(right[r:])
            
            return sorted_arr
        return merge_sort(nums)


        