def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start, mid):
        if A[start] < A[i]:
            mid = i
            break

    post(start+1, mid-1)
    post(mid, end)
    print(A[start])


A = []
while True:
    try:
        A += [int(input())]
    except:
        break
post(0, len(A)-1)