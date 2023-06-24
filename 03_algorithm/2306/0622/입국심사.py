import sys
input = sys.stdin.readline

N, M = map(int,input().split())
times = [int(input()) for _ in range(N)]
times.sort()

s = 0
e = times[-1] * M

answer = int(1e18)
while s <= e:
    mid = (s+e) // 2

    nums = 0
    for i in range(N):
        nums += mid // times[i]
    else:
        if nums >= M:
            answer = min(answer, mid)
            e = mid - 1
            continue
        s = mid + 1

print(answer)