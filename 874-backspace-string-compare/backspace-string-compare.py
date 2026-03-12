class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        S = 0
        T = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    S += 1
                    i -= 1
                elif S > 0:
                    S -= 1
                    i -= 1
                else:
                    break
            
            while j >= 0:
                if t[j] == '#':
                    T += 1
                    j -= 1
                elif T > 0:
                    T -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            if (i>=0) != (j >= 0):
                return False
            
            i -= 1
            j -= 1
        
        return True

        