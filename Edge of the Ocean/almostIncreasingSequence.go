func almostIncreasingSequence(sequence []int) bool {
	screwups, tailIndex := 0, 0
	for i := 1; i < len(sequence); i++ {
		if sequence[tailIndex] < sequence[i] {
			tailIndex = i
		} else {
			if tailIndex == 0 || sequence[i] > sequence[tailIndex - 1] {
				tailIndex = i
			}
			screwups++
		}
	}
	return screwups == 1
}
