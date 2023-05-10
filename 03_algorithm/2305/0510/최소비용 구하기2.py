import sys
input = sys.stdin.readline


def findMinIdx():
    idx = 0
    minValue = INF
    for i in range(1,N+1):
        if not visited[i] and minValue > distance[i]:
            minValue = distance[i]
            idx = i
    return idx


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i,dis in graph[start]:
        distance[i] = min(distance[i], dis)

    # 처음 시작 빼고
    for _ in range(N-1):
        now = findMinIdx()
        visited[now] = True
        for next, dis in graph[now]:
            distance[next] = min(distance[next], dis + distance[now])


N = int(input())
M = int(input())
INF = 1e11
distance = [INF] * (N+1)
visited = [False] * (N+1)
graph=[[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

S, E = map(int,input().split())
dijkstra(S)
print(distance[E])