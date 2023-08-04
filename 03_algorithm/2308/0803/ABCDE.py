import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x, d):
    if d == 4:
        return True
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            if dfs(nx, d+1):
                return True
            visited[nx] = False
    return False

N, M = map(int,input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for i in range(N):
    visited = [False] * N
    visited[i] = True
    if dfs(i, 0):
        ans = 1
        break

print(ans)