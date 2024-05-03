class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        map = {}
        res = []
        
        for i in range(len(nums2) -1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                map[nums2[i]] = stack[-1]

            stack.append(nums2[i])

        for num in nums1:
            res.append(map.get(num, -1))

        return res    



