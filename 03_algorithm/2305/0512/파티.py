import sys
import heapq
input = sys.stdin.readline
INF = int(1e11)

def dijkstra(S, distanceList, visited, pq):
    heapq.heappush(pq, (0, S))
    while pq:
        dis, now = heapq.heappop(pq)

        if visited[now]: continue
        visited[now] = True

        for next, next_distance in graph[now]:
            distanceList[next] = min(distanceList[next], next_distance + dis)
            heapq.heappush(pq, (distanceList[next], next))

N, M, X = map(int,input().split())
# N: 학생수, M: 도로의 수, X: 파티가 열리는 곳
graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j, t = map(int,input().split())
    graph[i].append((j,t))

visited = [False] * (N+1)
returnDistance = [INF] * (N+1)
returnDistance[X] = 0 # 파티가 열리는 곳에서 시작
dijkstra(X, returnDistance, visited, [])

result = [0] * (N+1)
for i in range(1, N+1):
    if i == X: continue
    distance = [INF] * (N+1)
    visited = [False] * (N+1)
    distance[i] = 0

    dijkstra(i, distance, visited, [])
    result[i] = returnDistance[i] + distance[X]
print(max(result))
