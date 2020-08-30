class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = list()
        for i in range(len(nums)):
            less = list()
            for j in nums:
                if j < nums[i]:
                    less.append(j)
            arr.append(len(less))xx
            less.clear()
        return arr