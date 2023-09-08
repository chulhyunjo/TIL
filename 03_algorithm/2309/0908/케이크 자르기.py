import sys
input = sys.stdin.readline

N, M, L = map(int,input().split())
cuts = [int(input()) for _ in range(M)] + [L]

for _ in range(N):
    q = int(input())

    s = 1
    e = L
    answer = 0
    while s <= e:
        mid = (s+e) // 2
        pre = 0
        cnt = 0
        for i in range(M+1):
            now = cuts[i]
            length = now - pre
            if length >= mid:
                pre = now
                cnt += 1
        if cnt > q:
            answer = max(mid, answer)
            s = mid + 1
        else:
            e = mid - 1
    print(answer)
