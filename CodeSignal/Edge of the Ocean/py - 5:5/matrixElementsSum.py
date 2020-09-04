def matrixElementsSum(matrix):
    thesum, bannedcols = 0, set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                bannedcols.add(j)
            if j not in bannedcols:
                thesum += matrix[i][j]
    return thesum