int adjacentElementsProduct(std::vector<int> inputArray) {
    int largestProduct = inputArray[0] * inputArray[1];
    for (int i = 0; i < inputArray.size() - 1; i++) {
        int newProduct = inputArray[i] * inputArray[i+1];
        if (largestProduct < newProduct) {
            largestProduct = newProduct;
        }
    }
    return largestProduct;
}
