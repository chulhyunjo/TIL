N, M = map(int,input().split())
numbers = list(map(int,input().split()))

s = 0
e = 10000
answer = 0
while s<=e:
    mid = (s+e) // 2

    min_num = numbers[0]
    max_num = numbers[0]
    cnt = 0
    for i in range(1, N):
        min_num = min(min_num, numbers[i])
        max_num = max(max_num, numbers[i])
        if max_num - min_num >= mid:
            cnt += 1
            max_num = min_num = numbers[i]
    if cnt >= M:
        answer = mid
        s = mid + 1
    else:
        e = mid - 1

print(answer)