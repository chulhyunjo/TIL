partition(A[], p, r)
    x <- A[r]
    i <- p - 1

    for j in p -> r - 1
        if A[j] <= x
            i++, swap(A[i], A[j])

    swap(A[i+i], A[r])
    Return i+1