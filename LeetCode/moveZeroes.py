class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastPoz = 0;
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastPoz] = nums[i]
                lastPoz += 1
        for i in range(lastPoz,len(nums)):
            nums[i] = 0