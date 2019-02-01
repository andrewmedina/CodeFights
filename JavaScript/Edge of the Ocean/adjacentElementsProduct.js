const adjacentElementsProduct = inputArray => {
    let greatest = inputArray[0] * inputArray[1];
    for (let i = 1; i < inputArray.length - 1; i++) {
        if (inputArray[i] * inputArray[i + 1] > greatest) greatest = inputArray[i] * inputArray[i + 1];
    }
    return greatest;
};