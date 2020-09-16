class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        isX = True
        grid = [[" " for _ in range(3)] for _ in range(3)]
        
        def isWinner(thegrid):
            for i in range(3):
                xsInRow, osInRow = 0, 0
                for j in range(3):
                    if thegrid[i][j] == "X":
                        xsInRow += 1
                    elif thegrid[i][j] == "O":
                        osInRow += 1
                if xsInRow == 3:
                    return "A"
                elif osInRow == 3:
                    return "B"
            for i in range(3):
                xsInCol, osInCol = 0, 0
                for j in range(3):
                    if thegrid[j][i] == "X":
                        xsInCol += 1
                    elif thegrid[j][i] == "O":
                        osInCol += 1
                if xsInCol == 3:
                    return "A"
                elif osInCol == 3:
                    return "B"
            if (thegrid[0][0] == "X" and thegrid[1][1] == "X" and thegrid[2][2] == "X") or (thegrid[0][2] == "X" and thegrid[1][1] == "X" and thegrid[2][0] == "X"):
                return "A"
            elif (thegrid[0][0] == "O" and thegrid[1][1] == "O" and thegrid[2][2] == "O") or (thegrid[0][2] == "O" and thegrid[1][1] == "O" and thegrid[2][0] == "O"):
                return "B"
            for x in thegrid:
                for el in x:
                    if el == " ":
                        return "Pending"
            return "Draw"
        
        for move in moves:
            grid[move[0]][move[1]] = "X" if isX else "O"
            isX = not isX
        return isWinner(grid)