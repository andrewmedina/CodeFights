func allLongestStrings(inputArray []string) []string {
    longest := 0
    for i := 0; i < len(inputArray); i++ {
        if len(inputArray[i]) > longest {
            longest = len(inputArray[i])
        }
    }
    var finalArray []string
    for j := 0; j < len(inputArray); j++ {
        if len(inputArray[j]) == longest {
            finalArray = append(finalArray, inputArray[j])
        }
    }
    return finalArray
}
