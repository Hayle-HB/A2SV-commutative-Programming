class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime = set()

        def find_prime(num):
            ans = []

            d = 2

            while d * d <= num:

                while num % d == 0:
                    ans.append(d)
                    num //= d
                
                d += 1
            if num > 1:
                ans.append(num)
            return ans
        
        for num in nums:
            curr = find_prime(num)
            for x in curr:
                prime.add(x)
        return len(prime)