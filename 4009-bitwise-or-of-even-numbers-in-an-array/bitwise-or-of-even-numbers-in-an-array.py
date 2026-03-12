class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        r = 0
        for i in nums:
            if i % 2 == 0:
                r = r | i
        return r