class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroSeen = False
        for i in range(len(arr)):
            if arr[i] == 0 and not zeroSeen and i+1 != len(arr):
                for j in range(len(arr)-2,i,-1):
                    arr[j+1] = arr[j]
                arr[i+1] = 0
                zeroSeen = True
            else:
                zeroSeen = False