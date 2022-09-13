t = int(input())
for tc in range(1,t+1):
    n = int(input())
    array = list(map(int, input().split()))
    min_dis = 100001
    cnt = 0
    for dis in range(n):
        if abs(array[dis]) < min_dis:
            min_dis = abs(array[dis])

    for dis in array:
        if abs(dis) == min_dis:
            cnt += 1

    print(f'#{tc} {min_dis} {cnt}')
