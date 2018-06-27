func makeArrayConsecutive2(statues []int) int {
    largest, smallest := 0, 20;
    for _, i := range statues {
        if (i > largest) {
            largest = i;
        }
        if (i < smallest) {
            smallest = i;
        }
    }
    return 1 + largest - smallest - len(statues);
}
