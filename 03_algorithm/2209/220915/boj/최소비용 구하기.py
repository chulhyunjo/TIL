import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,N+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = min(distance[i[0]],i[1])

    for _ in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for next in graph[now]:
            cost = distance[now] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[]for _ in range(N+1)]
visited = [False] * (N+1)
INF = int(1e11)
distance = [INF] * (N+1)
for _ in range(M):
    s, e, c= map(int,input().rstrip().split())
    graph[s].append((e,c))

a, b = map(int,input().rstrip().split())
dijkstra(a)
print(distance[b])