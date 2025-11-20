class Solution:
    def reverseVowels(self, s: str) -> str:
        v = []
        for i in s:
            if i in 'AEIOUaeiou':
                v.append(i)
        v.reverse()
        res = ""
        j = 0 
        for i in s :
            if i in 'AEIOUaeiou':
                res += v[j]
                j += 1
            else:
                res += i
        return(res)
            
        
            

        