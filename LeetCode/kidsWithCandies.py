class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr, themax = [], max(candies)
        for i in candies:
            arr.append(i + extraCandies >= themax)
        return arr