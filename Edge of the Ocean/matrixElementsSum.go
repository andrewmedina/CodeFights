func matrixElementsSum(matrix [][]int) int {
    sum := 0
    for row := 0; row < len(matrix[0]); row++ {
        for col := 0; col < len(matrix); col++ {
            if matrix[col][row] == 0 {
                break;
            }
            sum += matrix[col][row]
        }
    }
    return sum
}
