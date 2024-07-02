class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) <= 1:
            return False
        counter = Counter(deck)
        g = reduce(gcd, counter.values())

        return g >= 2
        