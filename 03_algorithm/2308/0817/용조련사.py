import heapq
N, M = map(int,input().split())
dragons = list(map(int,input().split()))

pq = []
for i in range(N):
    heapq.heappush(pq, (dragons[i], i+1))

last = pq[0][0]
answer = []
while pq:
    power, idx = heapq.heappop(pq)
    if power - last > M:
        break
    else:
        answer.append(idx)
        last = power

if len(answer) == N:
    print('YES')
    print(*answer)
else:
    print('NO')