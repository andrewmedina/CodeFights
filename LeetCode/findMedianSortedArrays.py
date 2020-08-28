class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        median = (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2 - 1)]) / 2 if len(arr) % 2 == 0 else arr[int(math.floor(len(arr) / 2))]
        return median