class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        inds, ans = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)], 0
        if S == 0:
            for i in range(len(inds) - 1):
                w = inds[i+1] - inds[i] - 1
                ans += w * (w+1) / 2
            return int(ans)
        for i in range(1, len(inds) - S):
            j = i + S - 1
            left, right = inds[i] - inds[i-1], inds[j+1] - inds[j]
            ans += left * right
        return int(ans)