for tc in range(1,int(input())+1):
    n = int(input())
    arr = list(map(int,input().split()))

    cnt = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    print(f'#{tc} {cnt}')