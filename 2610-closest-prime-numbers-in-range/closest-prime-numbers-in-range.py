from typing import List
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(limit**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
            return [i for i in range(limit + 1) if is_prime[i]]
        
        if right < 2:
            return [-1, -1]
        
        primes = sieve(right)
        
        primes = [p for p in primes if left <= p <= right]
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_diff = float('inf')
        result = [-1, -1]
        for i in range(len(primes) - 1):
            p1 = primes[i]
            p2 = primes[i + 1]
            if p2 - p1 < min_diff:
                min_diff = p2 - p1
                result = [p1, p2]
        
        return result