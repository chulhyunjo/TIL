import sys
import heapq
input = lambda: sys.stdin.readline()

N, M = map(int,input().split())
order = [[] for _ in range(N+1)]
degree = [0] * (N+1)

pq = []
for _ in range(M):
    a, b = map(int,input().split())
    order[a].append(b)
    degree[b] += 1

for i in range(1,N+1):
    if degree[i] == 0:
        heapq.heappush(pq, i)

answer = []
while pq:
    now = heapq.heappop(pq)
    answer.append(now)
    for nxt in order[now]:
        degree[nxt] -= 1
        if degree[nxt] == 0:
            heapq.heappush(pq,nxt)

print(*answer)