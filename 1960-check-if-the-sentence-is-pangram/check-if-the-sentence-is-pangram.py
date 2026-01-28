class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        is_pangram = True
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if i not in sentence.lower():
                is_pangram = False
                break
        return is_pangram 

        
        