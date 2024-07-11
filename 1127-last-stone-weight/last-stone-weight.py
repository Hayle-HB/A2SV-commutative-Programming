import heapq
class Solution:
    def lastStoneWeight(self, arr: List[int]) -> int:
        n = len(arr)
        arr = [-num for num in arr]
        heapq.heapify(arr)

        while len(arr) > 1:
            _max1 = -heapq.heappop(arr)
            _max2 = -heapq.heappop(arr)

            if _max1 != _max2:
                heapq.heappush(arr, -(_max1 - _max2))

        return -arr[0] if arr else 0
        