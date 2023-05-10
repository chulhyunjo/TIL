import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
INF = 10 ** 7

V, E = map(int,input().rstrip().split())
S = int(input()) # 출발 지점

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().rstrip().split())
    graph[u].append((v,w))

dis = [INF]*(V+1)
dis[S] = 0
visited = [False] * (V+1)
def dijkstra(now):
    visited[now] = True
    for next, d in graph[now]:
        dis[next] = min(dis[next], dis[now] + d)

    mIdx = 0
    minDis = INF
    for i in range(1,V+1):
        if not visited[i] and dis[i] < minDis:
            mIdx = i
            minDis = dis[i]
    if mIdx:
        dijkstra(mIdx)

dijkstra(S)
for i in range(1, V+1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])