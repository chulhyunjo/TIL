T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input()))

    cnt = 0
    result = 0
    for i in arr:
        if i == 1: # 1일 경우 cnt + 1
            cnt += 1
        else: # 0 일 경우 연속이 아니므로 0으로 초기화
            cnt = 0
        if cnt > result: # 가장 큰 값 result
            result = cnt

    print(f'#{tc} {result}')