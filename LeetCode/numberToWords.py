class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        singDict = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }      
        tyDict = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        bigDict = {
            1: "Thousand",
            2: "Million",
            3: "Billion"
        }
        res = list()
        split = [int(d) for d in str(num)]
        while len(split) % 3 != 0:
            split.insert(0,0)
        x = [split[i:i + 3] for i in range(0, len(split), 3)]
        xLen = len(x) - 1
        for i in range(0,len(x)):
            for j in range(0,len(x[i])):
                if j == 0:
                    if x[i][j] == 0:
                        continue
                    res.append(singDict[x[i][j]] + " Hundred")
                elif j == 1:
                    if x[i][j] > 1:
                        res.append(tyDict[x[i][j]])
                elif j == 2:
                    if x[i][j-1] == 1:
                        if x[i][j] == 0:
                            res.append("Ten")
                        elif x[i][j] == 1:
                            res.append("Eleven")
                        elif x[i][j] == 2:
                            res.append("Twelve")
                        elif x[i][j] == 3:
                            res.append("Thirteen")
                        elif x[i][j] == 5:
                            res.append("Fifteen")
                        elif x[i][j] == 8:
                            res.append("Eighteen")
                        else:
                            res.append(singDict[x[i][j]] + "teen")
                    elif x[i][j] == 0:
                        continue
                    else:
                        res.append(singDict[x[i][j]])
            if xLen > 0 and (x[i][0] > 0 or x[i][1] > 0 or x[i][2] > 0):
                res.append(bigDict[xLen])
            xLen -= 1
        return " ".join(res)