class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        if not word[0].isupper():
            return False
        for i in range(1,len(word)):
            if word[i].isupper():
                return False
        return True
                
                