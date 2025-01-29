class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        added = 1
        right = len(digits)-1
        while added and right >= 0:
            digits[right] += added

            if digits[right] == 10:
                digits[right] = 0
                added = 1
            else:
                added = 0
            right -= 1

        if added:
            return [1] + digits
        else:
            return digits



        