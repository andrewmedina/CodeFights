class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev, reg = str(x)[::-1], str(x)
        for i in range(len(reg)):
            if reg[i] != rev[i]:
                return False
        return True