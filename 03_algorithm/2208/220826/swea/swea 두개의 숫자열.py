for tc in range(1,int(input())+1):
    n, m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    if n > m:
        n, m = m, n
        arr1, arr2 = arr2, arr1

    result = 0
    for i in range(m-n+1):
        mult = 0
        for j in range(n):
            mult += arr1[j] * arr2[i+j]
        result = max(result,mult)

    print(f'#{tc} {result}')