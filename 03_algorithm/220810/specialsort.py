for tc in range(1,int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1):
        findV = i
        for j in range(i+1,n):
            if i % 2:
                if arr[j] < arr[findV]:
                    findV = j
            else:
                if arr[j] > arr[findV]:
                    findV = j
        arr[i], arr[findV] = arr[findV], arr[i]
    print(f'#{tc}', end = ' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()