import sys
input = sys.stdin.readline

K, N = map(int,input().split())
lines = [int(input()) for _ in range(K)]

s = 1
e = max(lines)
answer = 0
while s<=e:
    mid = (s+e)//2
    cnt = 0
    for l in lines:
        cnt += l // mid

    if cnt >= N:
        answer = mid
        s = mid + 1
    else:
        e = mid - 1

print(answer)