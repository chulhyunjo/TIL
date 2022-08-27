for tc in range(1,int(input())+1):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort(reverse = True)
    result = 0
    for i in range(m):
        result += arr[i]

    print(f'#{tc} {result}')