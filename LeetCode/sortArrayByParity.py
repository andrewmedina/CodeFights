class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        last, track = 0, list()
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[last] = A[i]
                last += 1
            else:
                track.append(A[i])
        for i in range(last,len(A)):
            A[i] = track.pop()
        return A