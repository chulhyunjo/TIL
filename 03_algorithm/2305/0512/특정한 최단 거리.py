import heapq
import sys

input = sys.stdin.readline
INF = int(1e11)

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]


def dijkstra(S, distance, visited, pq):
    heapq.heappush(pq, (0, S))
    distance[S] = 0

    while pq:
        dis, now = heapq.heappop(pq)
        if dis > distance[now]: continue
        if visited[now]: continue
        visited[now] = True
        for next, nextDis in graph[now]:
            distance[next] = min(distance[next], dis + nextDis)
            heapq.heappush(pq, (distance[next], next))


for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
distance = [INF] * (N + 1)  # 시작지점에서 최단 거리
v1_distance = [INF] * (N + 1)
v2_distance = [INF] * (N + 1)

dijkstra(1, distance, [False] * (N + 1), [])
if distance[N] == INF or distance[v1] == INF or distance[v2] == INF:
    print(-1)
else:
    dijkstra(v1, v1_distance, [False] * (N + 1), [])
    dijkstra(v2, v2_distance, [False] * (N + 1), [])

    # 시작 지점 -> v1 -> v2 -> 도착 or 시작 지점 -> v2 -> v1 -> 도착

    result = min(distance[v1] + v1_distance[v2] + v2_distance[N], distance[v2] + v2_distance[v1] + v1_distance[N])
    print(result)