import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
graph = [[] * i for i in range(n+1)]
visited = []

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(a):
    visited.append(a)
    for i in graph[a]:
        if i not in visited:
            dfs(i)
cnt = 0
for i in range(1, n+1):
    if i not in visited:
        dfs(i)
        cnt += 1
print(cnt)