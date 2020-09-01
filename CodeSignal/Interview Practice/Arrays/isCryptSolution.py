def isCryptSolution(crypt, solution):
    thedict = dict()
    for i in solution:
        thedict[i[0]] = i[1]
    arr1 = []
    for i in crypt:
        arr2 = []
        for j in i:
            arr2.append(thedict[j])
        arr1.append("".join(arr2))
    for i in arr1:
        if i[0] == "0" and len(i) > 1:
            return False
    return int(arr1[0]) + int(arr1[1]) == int(arr1[2])