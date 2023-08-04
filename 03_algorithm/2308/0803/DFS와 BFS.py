from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for nx in sorted(graph[x]):
        if not visited[nx]:
            dfs(nx)

def bfs(x):
    queue = deque([x])
    while queue:
        x = queue.popleft()
        print(x, end = ' ')
        for nx in sorted(graph[x]):
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
dfs(V)

print()

visited = [False] * (N+1)
visited[V] = True
bfs(V)