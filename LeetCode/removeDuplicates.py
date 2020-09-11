class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        track = dict()
        for i in nums:
            if i not in track:
                track[i] = 1
            else:
                track[i] += 1
        for i in track:
            onlyone = track[i]
            while onlyone > 1:
                nums.remove(i)
                onlyone -= 1