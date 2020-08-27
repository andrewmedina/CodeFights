class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum,track = 0,list()
        for i in range(0,len(nums)):
            print(i,nums[i])
            runsum = nums[i]+runsum
            track.append(runsum)
        return track