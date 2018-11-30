func sortByHeight(a []int) []int {
    for i := 0; i < len(a); i++ {
        if a[i] != -1 {
            m, idx := a[i], i
            for j := i + 1; j < len(a); j++ {
                if a[j] != -1 && a[j] < m {
                    m, idx = a[j], j
                }
            }
            if idx != i {
                tmp := a[i]
                a[i], a[idx] = a[idx], tmp
            }
        }
    }
    return a
}
