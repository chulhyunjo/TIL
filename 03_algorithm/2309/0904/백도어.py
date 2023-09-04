import heapq
import sys
input = sys.stdin.readline
INF = int(1e10)

def dijsktra():
    pq = [(0,0)]
    while pq:
        now_dis, now = heapq.heappop(pq)
        if visited[now]: continue
        visited[now] = True
        for nxt, nxt_dis in graph[now]:
            if sight[nxt]: continue
            dis = now_dis + nxt_dis
            if distance[nxt] <= dis: continue
            distance[nxt] = dis
            heapq.heappush(pq,(dis, nxt))

N, M = map(int,input().split()) # N:분기점 수, M: 길의 수
sight = list(map(int,input().split()))
sight[N-1] = 0
graph = [[] for _ in range(N)]
parents = list(range(N))

for _ in range(M):
    a, b, t = map(int,input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))

distance = [INF] * N
visited = [False] * N
distance[0] = 0

dijsktra()
print(distance[N-1] if distance[N-1] != INF else -1)