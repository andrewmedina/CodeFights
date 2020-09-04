def commonCharacterCount(s1, s2):
    comdict, thesum = dict(), 0
    for i in s1:
        if i not in comdict:
            comdict[i] = 1
        else:
            comdict[i] += 1
    for i in s2:
        if i in comdict and comdict[i] != 0:
            thesum += 1
            comdict[i] -= 1
    return thesum
            