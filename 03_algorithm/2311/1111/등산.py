N = int(input())
station = []
for _ in range(N):
    a, b = map(int,input().split())
    station.append((a, b))

answer = 0
for i in range(N):
    start = station[i][0]
    nxt = station[i][1]
    if start >= nxt:
        start -= nxt
        for j in range(1, N):
            start += station[(i+j)%N][0]
            nxt = station[(i+j)%N][1]
            if start >= nxt:
                start -= nxt
            else:
                break
        else:
            answer += 1
    else:
        continue
print(answer)