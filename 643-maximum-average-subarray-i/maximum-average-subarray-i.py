class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = 0

        for i in range(k):
            m += nums[i]
        w = m
        for i in range(k,len(nums)):
            w = w + nums[i] - nums[i-k]

            if w > m:
                m = w
        return m/k

        