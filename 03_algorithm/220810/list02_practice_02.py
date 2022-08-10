for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1<<10):
        sum1 = 0
        cnt = 0
        for j in range(10):
            if i & (1<<j):
                sum1 += arr[j]
                cnt += 1
        if sum1 == 0 and cnt >= 1:
            result = 1
            break

    print(f'#{tc} {result}')