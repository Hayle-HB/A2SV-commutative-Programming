class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = {}
        for num1 in nums1:
            for num2 in nums2:
                dic[num1 + num2] = dic.get(num1 + num2, 0) + 1
        
        count = 0

        for num3 in nums3:
            for num4 in nums4:

                if -(num3 + num4) in dic:
                    count += dic[-(num3 + num4)]
        
        return count


        