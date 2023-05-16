import heapq
INF = 10**4
n, m, r = map(int,input().split())
items = [0]+list(map(int,input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int,input().split())
    graph[a].append([b,l])
    graph[b].append([a,l])

answer = 0
for start in range(1, n+1):
    pq = []
    distance = [INF] * (n+1)
    distance[start] = 0
    visited = [False] * (n+1)
    heapq.heappush(pq,(0,start))

    while pq:
        start_dis, start = heapq.heappop(pq)
        if visited[start]: continue
        visited[start] = True
        for next, next_dis in graph[start]:
            distance[next] = min(distance[next], start_dis+ next_dis)
            heapq.heappush(pq, (distance[next], next))
    sum1 = 0
    for i in range(1,n+1):
        if distance[i] <= m:
            sum1 += items[i]
    answer = max(answer, sum1)

print(answer)