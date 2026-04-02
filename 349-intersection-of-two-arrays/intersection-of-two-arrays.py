class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = []
        for i in nums1:
            if i in nums2 and i not in n:
                n.append(i)
        return n

        