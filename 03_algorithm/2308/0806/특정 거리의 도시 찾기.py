from collections import deque
import sys
input = sys.stdin. readline

def bfs(i):
    global result
    while queue:
        x, dis = queue.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                if dis + 1 == K:
                    result.add(nx)
                else:
                    queue.append((nx, dis+1))

N, M, K, X = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)

visited = [False] * (N+1)
result = set()
queue = deque([(X, 0)])
visited[X] = True
bfs(X)
if result:
    print(*sorted(result), sep='\n')
else:
    print(-1)