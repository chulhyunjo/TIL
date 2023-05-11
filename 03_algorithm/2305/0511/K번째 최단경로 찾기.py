import sys
import heapq
input = sys.stdin.readline
INF = 1e11

# N :도시 개수, M: 도시간의 도로 개수, K: K번째 최단 경로
N, M, K = map(int,input().rstrip().split())
graph = [[] for _ in range(N+1)]

distance = [[INF]*(K) for _ in range(N+1)]
# 1번 도시는 시작 도시

for _ in range(M):
    A, B, C = map(int,input().rstrip().split())
    graph[A].append((B, C))


pq = [(0,1)]
distance[1][0] = 0

while pq:
    dis, now = heapq.heappop(pq)
    for next, nextDis in graph[now]:
        d = dis + nextDis
        if distance[next][K-1] > d:
            distance[next][K-1] = d
            distance[next].sort()
            heapq.heappush(pq, [d, next])

for i in range(1, N+1):
    if distance[i][K-1] == INF:
        print(-1)
    else:
        print(distance[i][K-1])