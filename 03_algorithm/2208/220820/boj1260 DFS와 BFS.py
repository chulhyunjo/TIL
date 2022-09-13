from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dfs_list = []
bfs_list = []


def dfs(v):
    visit_d[v] = True
    dfs_list.append(v)
    for i in sorted(graph[v]):
        if not visit_d[i]:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visit_b[v] = True
    while queue:
        x = queue.popleft()
        bfs_list.append(x)
        for i in sorted(graph[x]):
            if not visit_b[i]:
                queue.append(i)
                visit_b[i] = True


n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit_d = [False] * (n+1)
visit_b = [False] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v)
bfs(v)

print(*dfs_list)
print(*bfs_list)