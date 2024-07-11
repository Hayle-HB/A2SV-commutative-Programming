class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = [(-frq, word) for word, frq in count.items()]
        heapq.heapify(heap)
        ans = []

        for _ in range(k):
            freq, word = heapq.heappop(heap)
            ans.append(word)
        
        return ans
