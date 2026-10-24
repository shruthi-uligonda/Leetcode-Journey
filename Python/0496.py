# Next Greater Element I

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                idx = stack.pop()
                greater[idx] = num
            stack.append(num)
        while stack:
            idx = stack.pop()
            greater[idx] = -1
        ans = []
        for num in nums1:
            ans.append(greater[num])
        return ans
