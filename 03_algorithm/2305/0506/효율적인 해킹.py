from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
graph = [[] for _ in range(N+1)]
answer = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

def bfs(X):
    global answer
    queue = deque()
    queue.append(X)
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                answer[next] += 1
                visited[next] = 1

for i in range(1,N+1):
    visited = [0] * (N+1)
    visited[i] = 1
    bfs(i)

maxCnt = max(answer)
for j in range(1,N+1):
    if answer[j] == maxCnt:
        print(j, end=' ')