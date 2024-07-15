class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        for num in nums:

            while heap and heap[0][0] + 1 < num:
                _, len_seq = heappop(heap)
                if len_seq < 3:
                    return False
            if not heap:
                heap.append([num, 1])
            else:
                if heap[0][0] == num:
                    heappush(heap, [num, 1])
                else:
                    _, len_seq = heappop(heap)
                    heappush(heap, [num, len_seq + 1])
        return all(p[1] >= 3 for p in heap)           
            