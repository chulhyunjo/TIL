import sys
import heapq
input = sys.stdin.readline
INF = int(1e11)

def dijkstra(pq, distance):
    visited = [False] * (n+1)
    while pq:
        nowDis, now = heapq.heappop(pq)
        if visited[now]: continue
        visited[now] = True
        for next, nextDis in city[now]:
            if nowDis + nextDis < distance[next]:
                distance[next] = nowDis + nextDis
                heapq.heappush(pq, (distance[next], next))


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    city = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int,input().split())
        city[a].append((b, d))
        city[b].append((a, d))

    findCity = []
    for _ in range(t):
        findCity.append(int(input()))

    distanceS = [INF] * (n+1)
    distanceS[s] = 0
    dijkstra([(0,s)], distanceS) # 시작점에서 최단 거리


    distanceG = [INF] * (n + 1)
    distanceG[g] = 0
    dijkstra([(0,g)], distanceG)

    distanceH = [INF] * (n + 1)
    distanceH[h] = 0
    dijkstra([(0, h)], distanceH)

    answer = []
    for find in findCity:
        if distanceS[g] + distanceG[h] + distanceH[find] == distanceS[find]:
            answer.append(find)
        elif distanceS[h] + distanceH[g] + distanceG[find] == distanceS[find]:
            answer.append(find)

    print(*sorted(answer))
