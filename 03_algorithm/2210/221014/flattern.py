for tc in range(1, 11):
    n = int(input())
    arr = list(map(int,input().split()))
    while n:
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
        if max(arr) - min(arr) <= 1:
            break
        n-=1
    print(f'#{tc} {max(arr) - min(arr)}')