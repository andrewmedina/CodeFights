def almostIncreasingSequence(sequence):
    dropped = False
    last = prev = min(sequence) - 1
    for i in sequence:
        if i <= last:
            if dropped:
                return False
            dropped = True
            if i <= prev:
                prev = last
            else:
                prev = last = i
        else:
            prev, last = last, i
    return True