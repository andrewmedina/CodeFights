func isLucky(n int) bool {
    s, a, b := strconv.Itoa(n), 0, 0
    for _, i := range s[:len(s) / 2] {
        a += int(i)
    }
    for _, i := range s[len(s) / 2:] {
        b += int(i)
    }
    return a == b
}
