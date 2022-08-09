t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 1
    result = 1
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > result:
            result = cnt

    print(f'#{tc} {result}')