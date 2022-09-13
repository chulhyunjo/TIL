for tc in range(1, int(input())+1):
    n, m  = map(int,input().split())
    arr = list(map(int,input().split()))

    for i in range(m):
        x = arr.pop(0)
        arr.append(x)

    print(f'#{tc} {arr[0]}')