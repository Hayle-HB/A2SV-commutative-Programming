class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        is_pos = num > 0
        
        num = abs(num)
        num_str = str(num)
        
        if is_pos:
            sorted_chars = sorted(num_str)
        else:
            sorted_chars = sorted(num_str, reverse=True)
        
        if is_pos:
            for i in range(len(sorted_chars)):
                if sorted_chars[i] != '0':
                    sorted_chars[0], sorted_chars[i] = sorted_chars[i], sorted_chars[0]
                    break
        
        result_str = "".join(sorted_chars)
        
        result = int(result_str)
        if not is_pos:
            result = -result
        
        return result
