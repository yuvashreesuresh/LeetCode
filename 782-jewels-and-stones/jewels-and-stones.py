class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        js = set(jewels)
        c = 0
        for i in stones:
            if i in js:
                c += 1
        return c
        