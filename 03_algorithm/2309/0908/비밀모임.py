import heapq
import sys
input = sys.stdin.readline
INF = int(1e7)

def dijkstra(s):
    pq = [(0, s)]
    visited = [False] * (N+1)
    d = [INF] * (N+1)
    d[s] = 0
    while pq:
        now_dis, now = heapq.heappop(pq)
        if visited[now]: continue
        visited[now] = True
        for nxt, dis in graph[now]:
            nxt_dis = dis + now_dis
            if d[nxt] <= nxt_dis: continue
            d[nxt] = nxt_dis
            heapq.heappush(pq, (nxt_dis, nxt))
    return d

for _ in range(int(input())):
    N, M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int,input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    K = int(input())
    friends = list(map(int,input().split()))

    distance = [0] * (N+1)
    for i in friends:
        n_d = dijkstra(i)
        for j in range(1, N+1):
            distance[j] += n_d[j]
    print(distance[1:].index(min(distance[1:]))+1)