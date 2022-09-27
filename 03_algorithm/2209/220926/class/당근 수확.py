T = int(input())
for tc in range(1, T+1):
    n = int(input())
    carrot = list(map(int,input().split()))

    result = 1000
    result_idx = 0
    for i in range(1,n-1):
        sum1 = sum2 = 0
        for j in range(i):
            sum1 += carrot[j]
        for j in range(i,n):
            sum2 += carrot[j]
        if abs(sum1 - sum2) < result:
            result = abs(sum1-sum2)
            result_idx = i

    print(f'#{tc} {result_idx} {result}')