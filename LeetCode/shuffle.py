class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = len(nums) // 2
        x, y, arr = nums[:mid], nums[mid:], list()
        lenx, leny = len(x), len(y)
        for i in range(lenx+leny):
            arr.append((x if i % 2 == 0 else y).pop(0))
        return arr
            