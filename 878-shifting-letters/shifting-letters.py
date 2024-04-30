class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def shift(c, shift_val):
            if shift_val > 26:
                shift_val = shift_val % 26
            
            char_val = ord(c)-96 + shift_val

            if(char_val > 26):
                char_val = char_val - 26
            return chr(char_val+96)
            


        prifix_right = sum(shifts)
        s = list(s)

        for i in range(len(s)):
            s[i] = shift(s[i], prifix_right)
            prifix_right -= shifts[i]



        return ''.join(s)
        

        