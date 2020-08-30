def firstNotRepeatingCharacter(s):
    repeated = dict()
    for i in s:
        repeated[i] = i in repeated
    for i in s:
        if repeated[i] == False:
            return i
    return "_"