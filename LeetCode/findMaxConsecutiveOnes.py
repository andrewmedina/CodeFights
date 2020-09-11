class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        themax,current = 0,0
        for i in nums:
            if i == 1:
                current += 1
            else:
                current = 0
            if current > themax:
                themax = current
        return themax