def adjacentElementsProduct(inputArray):
    max_prod = inputArray[0] * inputArray[1]
    for i in range(len(inputArray)-1):
        prod = inputArray[i] * inputArray[i+1]
        if prod > max_prod:
            max_prod = prod
    return max_prod
