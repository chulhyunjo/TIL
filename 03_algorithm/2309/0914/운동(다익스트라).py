import heapq
import sys
input = sys.stdin.readline
INF = 1<<31

def dijkstra():
    pq = []
    distance = [[INF] * (V + 1) for _ in range(V + 1)]
    for a in range(1, V+1):
        for b, c in graph[a]:
            distance[a][b] = c
            heapq.heappush(pq, (c, b, a))
    while pq:
        now_dis, now, first = heapq.heappop(pq)
        if now == first:
            return now_dis
        if now_dis > distance[first][now]: continue
        for nxt, nxt_dis in graph[now]:
            dist = now_dis + nxt_dis
            if distance[first][nxt] > dist:
                distance[first][nxt] = dist
                heapq.heappush(pq,(dist, nxt, first))
    return -1


V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

print(dijkstra())