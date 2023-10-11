from collections import deque

def dfs(x):
    dfsResult.append(x)
    visited_dfs[x] = True
    for nx in sorted(graph[x]):
        if not visited_dfs[nx]:
            dfs(nx)

def bfs(x):
    queue = deque([x])
    visited_bfs[x] = True
    while queue:
        x = queue.popleft()
        bfsResult.append(x)
        for nx in sorted(graph[x]):
            if not visited_bfs[nx]:
                visited_bfs[nx] = True
                queue.append(nx)

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfsResult = []
visited_dfs = [False] * (N+1)

bfsResult = []
visited_bfs = [False] * (N+1)

dfs(V)
bfs(V)
print(*dfsResult)
print(*bfsResult)