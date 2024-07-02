class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if b == 0:
                return a 
            return gcd(b, a % b)
        if len(deck) <= 1:
            return False

        count = Counter(deck)
        expect = min(count.values())
        print(count)
        for num in count.values():
            expect = gcd(num, expect)
            if expect == 1:
                return False
        return True
        