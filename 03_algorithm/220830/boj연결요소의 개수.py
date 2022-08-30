import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    for q in graph[v]:
        if not visited[q]:
            dfs(q)


n, m = map(int,input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
visited = [False] * (n+1)
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)