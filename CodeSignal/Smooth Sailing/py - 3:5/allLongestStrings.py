def allLongestStrings(inputArray):
    maxlen = max(len(i) for i in inputArray)
    return [i for i in inputArray if len(i) == maxlen]