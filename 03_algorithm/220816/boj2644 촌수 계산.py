import sys
from collections import deque
input = sys.stdin.readline

def bfs(v, target):
    queue = deque()
    queue.append([v,0])
    while queue:
        v, cnt = queue.popleft()

        if v == target:
            return cnt
        if not visited[v]:
            visited[v] = True
            for i in graph[v]:
                if not visited[i]:
                    queue.append([i, cnt+1])
    return -1


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
q, w = map(int,input().split())

m = int(input())
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(q,w))