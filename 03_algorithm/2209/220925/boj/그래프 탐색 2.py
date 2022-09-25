from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs():
    while queue:
        now, cnt = queue.popleft()
        result[now] = cnt
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i,cnt+1))

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append((1,0))
result = [-1] * (n+1)
visited = [0] * (n+1)
visited[1] = 1
bfs()

q = int(input())
for _ in range(q):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    visited = [0] * (n + 1)
    visited[1] = 1
    queue.append((1,0))
    bfs()
    print(*result[1:])