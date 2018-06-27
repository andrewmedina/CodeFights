func almostIncreasingSequence(sequence []int) bool {
	screwups, tail := 0, 0
	for i := 1; i < len(sequence); i++ {
		if sequence[tail] < sequence[i] {
			tail = i
		} else {
			if tail == 0 || sequence[i] > sequence[tail - 1] {
				tail = i
			}
			screwups++
		}
	}
	return screwups == 1
}
