class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr = [char for char in s[::-1]]
        for i in t:
            if arr and i == arr[-1]:
                arr.pop()
        return len(arr) == 0
