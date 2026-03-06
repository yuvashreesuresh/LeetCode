class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            pos = ord(s[i]) - ord('a') + 1
            rev = 27 - pos
            val = rev * (i+1)
            total = total + val
        return total
        