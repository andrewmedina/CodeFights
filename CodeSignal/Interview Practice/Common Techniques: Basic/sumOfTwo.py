def sumOfTwo(a, b, v):
    diff = set()
    for i in range(len(a)):
        diff.add(v - a[i])
    for i in range(len(b)):
        if b[i] in diff:
            return True
    return False