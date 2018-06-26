func adjacentElementsProduct(inputArray []int) int {
    greatest := inputArray[0] * inputArray[1];
    for i := 1; i < len(inputArray) - 1; i++ {
        nextProd := inputArray[i] * inputArray[i + 1]
        if nextProd > greatest {
            greatest = nextProd
        }
    }
    return greatest
}
