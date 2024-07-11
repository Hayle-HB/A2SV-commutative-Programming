class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
        x = list(sorted(count.items(), key = lambda x: (-x[1], x[0])))
        ans = []
        for a, _ in x:
            ans.append(a)
            k -= 1
            if k == 0:
                break
        return ans