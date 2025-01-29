class Solution:
    def isPalindrome(self, x: int) -> bool:
        return list(str(x)) == list(str(x))[::-1]
        