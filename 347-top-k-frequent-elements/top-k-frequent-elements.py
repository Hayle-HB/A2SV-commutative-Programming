class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = Counter(nums)

            heap = [(-freq, num) for num, freq in count.items()]
            heapq.heapify(heap)
            
            ans = []
            for _ in range(k):
                    _, num = heapq.heappop(heap)
                    ans.append(num)



            return ans