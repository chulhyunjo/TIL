import heapq
import sys
input = sys.stdin.readline
INF = 10**9 + 1

def dijkstra(i):
    pq = [(0, i)]
    while pq:
        now_dis, now = heapq.heappop(pq)
        if now == e:
            return
        if visited[now]: continue
        visited[now] = True
        for nx, nx_dis in graph[now]:
            nd = now_dis + nx_dis
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(pq, (nd, nx))

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))

s, e = map(int,input().split())

visited = [False] * (N+1)
distance = [INF] * (N+1)
distance[s] = 0

dijkstra(s)
print(distance[e])
