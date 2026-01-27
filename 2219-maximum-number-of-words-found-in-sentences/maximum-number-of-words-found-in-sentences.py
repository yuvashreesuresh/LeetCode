class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c = 0
        for s in sentences:
            words = s.split()
            c = max(c,len(words))
        return c
        