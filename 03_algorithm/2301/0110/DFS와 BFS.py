from collections import deque
d_result = []
b_result = []

def dfs(s):
    d_result.append(s)
    d_visited[s] = 1
    for i in sorted(graph[s]):
        if not d_visited[i]:
            dfs(i)

def bfs(s):
    queue = deque()
    queue.append(s)
    b_visited[s] = 1
    while queue:
        now = queue.popleft()
        b_result.append(now)
        for i in sorted(graph[now]):
            if not b_visited[i]:
                b_visited[i] = 1
                queue.append(i)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

d_visited = [0] * (n+1)
b_visited = [0] * (n+1)

dfs(v)
bfs(v)
print(*d_result)
print(*b_result)
