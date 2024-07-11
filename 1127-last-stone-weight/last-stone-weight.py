from typing import List

class Solution:
    def lastStoneWeight(self, arr: List[int]) -> int:
        n = len(arr)
        
        def heapify(arr, n, i):
            l = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[l]:
                l = left
            if right < n and arr[right] > arr[l]:
                l = right
            
            if l != i:
                arr[l], arr[i] = arr[i], arr[l]
                return heapify(arr, n, l)
        
        def pop():
            _max = arr[0]
            arr[0], arr[-1] = arr[-1], arr[0]
            arr.pop()
            heapify(arr, len(arr), 0)
            return _max
        
        for i in range(len(arr)//2 - 1, -1, -1):
            heapify(arr, len(arr), i)
        
        while len(arr) > 1:
            first = pop()
            second = pop()
            if first != second:
                arr.append(abs(first - second))
                heapify(arr, len(arr), len(arr) - 1)
        
        return arr[0] if arr else 0
