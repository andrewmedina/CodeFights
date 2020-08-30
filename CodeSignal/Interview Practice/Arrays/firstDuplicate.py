def firstDuplicate(a):
    reps = set()
    for i in a:
        if i not in reps:
            reps.add(i)
        else:
            return i
    return -1