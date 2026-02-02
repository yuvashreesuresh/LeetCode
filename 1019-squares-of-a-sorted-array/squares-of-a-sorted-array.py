class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            n = nums[i]*nums[i]
            l.append(n)
        return sorted(l)
        