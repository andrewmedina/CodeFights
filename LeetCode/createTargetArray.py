class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()
        for i in range(len(nums)):
            res.insert(index[i],nums[i])
        return res