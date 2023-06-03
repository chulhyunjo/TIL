from collections import deque
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(S, D, graph, distance):
    pq = [(0,S)]
    distance[S] = 0

    while pq:
        nowDis, now = heapq.heappop(pq)
        if now == D:
            return nowDis
        for next, nextDis in graph[now]:
            d = nowDis + nextDis
            if distance[next] > d:
                distance[next] = d
                heapq.heappush(pq, (distance[next], next))

def bfs(s, graph):
    queue= deque()
    queue.append(s)

    while queue:
        now = queue.popleft()
        graphlength = len(graph[now])
        for idx in range(graphlength-1, -1, -1):
            next, nextDis = graph[now][idx]
            if distance[next] == distance[now] - nextDis:
                queue.append(next)
                del graph[now][idx]


while True:
    N, M = map(int,input().split())
    if N == M == 0: break

    graph = [[] for _ in range(N)]
    graph2 = [[] for _ in range(N)]
    S, D = map(int,input().split())

    for _ in range(M):
        U, V, P = map(int,input().split())
        graph[U].append((V,P))
        graph2[V].append((U,P))

    distance = [INF] * N
    dijkstra(S,D,graph,distance)
    if distance[D] == INF:
        print(-1)
    else:
        bfs(D, graph2)

        distance = [INF] * N
        dijkstra(D,S,graph2,distance)
        if distance[S] == INF:
            print(-1)
        else:
            print(distance[S])
