class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        track, high = 1, 1
        for i in range(1,len(nums)):
            track = 1 if nums[i] <= nums[i-1] else track + 1
            if track > high:
                high = track
        return high