class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rowLen, colLen = len(A), len(A[0])
        x = [[] for i in range(colLen)]
        for i in range(rowLen):
            for j in range(colLen):
                x[j].append(A[i][j])
        return x