const makeArrayConsecutive2 = statues => {
    let sorted = statues.slice().sort((a, b) => a - b), 
        count = 0;
    for (let i = sorted[0]; i < sorted[sorted.length - 1]; i++) {
        if (!sorted.includes(i)) count++;
    }
    return count;
};