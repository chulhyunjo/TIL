from collections import deque
def dfs(i):
    dfs_visited.append(i)
    visited_dfs[i] = 1
    for nx in sorted(graph[i]):
        if not visited_dfs[nx]:
            dfs(nx)

def bfs(i):
    queue = deque([i])
    visited_bfs[i] = 1
    while queue:
        x = queue.popleft()
        bfs_visited.append(x)
        for nx in sorted(graph[x]):
            if not visited_bfs[nx]:
                visited_bfs[nx] = 1
                queue.append(nx)


N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_visited = []
visited_dfs = [0] * (N+1)

bfs_visited = []
visited_bfs = [0] * (N+1)

dfs(V)
bfs(V)

print(*dfs_visited)
print(*bfs_visited)