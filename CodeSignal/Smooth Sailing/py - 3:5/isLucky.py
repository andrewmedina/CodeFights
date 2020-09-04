def isLucky(n):
    then = list(str(n))
    mid = len(then)//2
    first, second = then[:mid], then[mid:]
    sumfirst, sumsecond = sum(int(i) for i in first), sum(int(i) for i in second)
    return sumfirst == sumsecond