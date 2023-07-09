import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(x):
    heapq.heappush(pq, (0,x))
    while pq:
        nowDis, now = heapq.heappop(pq)
        if visited[now]: continue
        visited[now] = True
        for nxt, nxtDis in graph[now]:
            dis = nowDis + nxtDis
            if distance[nxt] > dis:
                distance[nxt] = dis
                heapq.heappush(pq, (dis, nxt))

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s, t = map(int,input().split())

distance = [INF] * (n+1)
visited = [False] * (n+1)
pq = []
dijkstra(s)
print(distance[t])