class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[1] - A[0] <= 0:
            return False
        increasing = True
        for i in range(1,len(A)):
            diff = A[i] - A[i-1]
            if diff == 0:
                return False
            if increasing:
                if diff < 0:
                    increasing = False
            else:
                if diff > 0:
                    return False
        if not increasing:
            return True
        return False