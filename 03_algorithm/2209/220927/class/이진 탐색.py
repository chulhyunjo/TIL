def find(s, e, target, d):
    global cnt
    move = 0
    if s<= e:
        mid = (s+e) // 2
        if target == A[mid]:
            cnt += 1
            return
        elif target < A[mid] and d!=1:
            e = mid - 1
            d = 1
            move = 1
        elif target > A[mid] and d!=2:
            s = mid + 1
            d = 2
            move = 1
    if move: find(s, e, target, d)

for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    cnt = 0
    for i in B:
        find(0, n-1, i, 0)
    print(f'#{tc} {cnt}')