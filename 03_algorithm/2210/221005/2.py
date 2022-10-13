T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i][0] < arr[j][0] and arr[i][1] >arr[j][1] or arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                result += 1

    print(f'#{tc} {result}')