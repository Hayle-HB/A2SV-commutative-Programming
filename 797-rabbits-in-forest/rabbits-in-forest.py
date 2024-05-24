from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        count = 0
        i = 0
        
        while i < len(answers):
            current = answers[i]
            group = 0

            while i < len(answers) and answers[i] == current:
                i += 1
                group += 1
            
            count += (current + 1) * ((group + current) // (current + 1))
        
        return count
