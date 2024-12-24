class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        count = Counter(arr)

        answer = set()

        for c in count:
            if count[c] > len(arr) // 3:
                answer.add(c)
        return list(answer)