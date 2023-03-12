import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(i):
    visited[i] = 1
    for next in graph[i]:
        if not visited[next]:
            dfs(next)

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
answer = 0

for i in range(1, n+1):
    if not visited[i]:
        answer += 1
        dfs(i)

print(answer)