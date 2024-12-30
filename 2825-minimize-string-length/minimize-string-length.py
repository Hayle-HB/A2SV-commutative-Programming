class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # Convert string to set to get unique characters
        unique_chars = set(s)
        # Return the number of unique characters
        return len(unique_chars)
