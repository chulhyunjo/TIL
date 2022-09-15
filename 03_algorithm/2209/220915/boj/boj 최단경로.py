from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(start):
    S = []
    heappush(S, (start,0))
    dis[start] = 0
    visited[start] = True
    while S:
        node, distance = heappop(S)
        if dis[node] < distance: continue
        for e, d in graph[node]:
            if dis[e] > d + distance:
                dis[e] = d + distance
                heappush(S, (e,d+distance))

V, E = map(int,input().split())
K = int(input()) # 시작 지점
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))
visited = [False] * (V+1)
INF = int(1e9)
dis = [INF] * (V+1)
dijkstra(K)
for i in range(1,len(dis)):
    if dis[i] == INF:
        print('INF')
    else:
        print(dis[i])