func commonCharacterCount(s1 string, s2 string) int {
    count, charMap := 0, make(map[rune]int) 
    for _, i := range s1 {
        charMap[i]++
    } 
    for _, i := range s2 {
        if charMap[i] >= 1 {
            charMap[i]--
            count++
        }
    }
    return count
}
