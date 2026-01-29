class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c = 0
        alt = 0
        for i in gain:
            c+=i
            alt = max(alt,c)
        return alt
        