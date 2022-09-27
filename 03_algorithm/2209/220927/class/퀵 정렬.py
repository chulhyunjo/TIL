def partition(l,r):
    pivot = A[l]
    i, j = l ,r
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j

def qsort(l,r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)

for tc in range(1, int(input())+1):
    n = int(input())
    A = list(map(int,input().split()))
    qsort(0, n-1)
    print(f'#{tc} {A[n//2]}')