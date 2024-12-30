class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return c == c[::-1]
