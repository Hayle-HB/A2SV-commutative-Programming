class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []


        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(comb, next_dig):
            if not next_dig:
                result.append(comb)
                return
            
            for letter in phone[next_dig[0]]:
                backtrack(comb + letter, next_dig[1:])
        
        backtrack("", digits)

        return result
        