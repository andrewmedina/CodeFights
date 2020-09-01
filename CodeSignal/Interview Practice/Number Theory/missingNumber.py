def missingNumber(arr):
    for i in range(max(arr)+1):
        if i not in arr:
            return i
    return max(arr)+1