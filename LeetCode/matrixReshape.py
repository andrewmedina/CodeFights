class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        track, thelength, tracklist = 0, 0, list()
        for i in range(0,len(nums)):
            for j in range(0,len(nums[i])):
                tracklist.append(nums[i][j])
            thelength += len(nums[i])
        if len(tracklist) < r * c:
            return nums
        final,sub = list(),list()
        for i in tracklist:
            sub.append(i)
            if len(sub) == c:
                final.append(sub)
                sub = list()
        return final