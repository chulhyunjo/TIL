for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int,input().split()))
    maxIdx = 0
    minIdx = 0

    for i in range(1,n):
        if arr[minIdx] > arr[i]:
            minIdx = i
        if arr[maxIdx] <= arr[i]:
            maxIdx = i

    print(f'#{tc} {maxIdx - minIdx if maxIdx - minIdx > 0 else -(maxIdx - minIdx)}')
