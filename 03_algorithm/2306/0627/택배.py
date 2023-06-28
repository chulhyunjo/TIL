import heapq
import sys
input = sys.stdin.readline
INF = int(2e6)

def dijkstra(i):
    pq = []
    heapq.heappush(pq, (0, i, i))
    while pq:
        nowDis, now, first = heapq.heappop(pq)
        if visited[now]: continue
        if first != i:
            answer[i-1][now-1] = first
        visited[now] = True
        for next, nextDis in graph[now]:
            dis = nowDis + nextDis
            if distance[next] > dis:
                distance[next] = dis
                if first == i:
                    heapq.heappush(pq, (dis, next, next))
                else:
                    heapq.heappush(pq, (dis, next, first))


N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, dis = map(int,input().split())
    graph[a].append((b,dis))
    graph[b].append((a,dis))

answer = [['-'] * N for _ in range(N)]

for i in range(1, N+1):
    distance = [INF] * (N+1)
    visited = [False] * (N+1)
    distance[i] = 0
    dijkstra(i)

for i in range(N):
    print(*answer[i])