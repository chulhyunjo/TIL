for tc in range(1,int(input())+1):
    k, n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    start = 0
    idx = 0
    result = 0
    while start < n:
        while idx < m and arr[idx] <= start+k:
            idx += 1
        start = arr[idx-1]
        if idx < m and start + k <arr[idx]:
            result = 0
            break
        result += 1
        if start + k >= n:
            break
    print(f'#{tc} {result}')
