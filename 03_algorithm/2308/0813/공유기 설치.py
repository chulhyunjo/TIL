import sys
input = sys.stdin.readline

N,C = map(int,input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
homes.sort()

start = 1
end = homes[-1] - homes[0]

answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = homes[0]
    for i in range(1, N):
        if mid <= homes[i] - current:
            current = homes[i]
            cnt += 1

    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)