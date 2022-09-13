for tc in range(1, int(input())+1):
    n, k = map(int,input().split())
    arr = list(range(1,13))
    result = 0
    for i in range(1<<n):
        sum1 = 0
        num = 0
        for j in range(n):
            if i & (1<<j):
                sum1 += arr[j]
                num += 1
            if num > n:
                break
        if sum1 == k and num == n:
            result += 1
    print(f'#{tc} {result}')
