class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0:
            return 0
        tokens.sort()
        print(tokens)
        score = 0

        left = 0
        right = len(tokens)-1
        max_score = 0
        while left <= right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left +=1
                max_score = max(max_score, score)
            else:
                if score > 0:
                    power += tokens[right]
                    right -= 1
                    score -= 1
                else:
                    break
        return max_score


        