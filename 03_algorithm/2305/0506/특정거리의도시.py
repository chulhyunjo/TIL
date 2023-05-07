import sys
from collections import deque
input = sys.stdin.readline

# N: 도시개수, M:도로 개수, K: 거리 정보, X: 출발 도시 정보
N, M, K, X = map(int,input().rstrip().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)

visited = [0] * (N+1)
visited[X] = 1
answer = []
def bfs(s):
    queue = deque()
    queue.append((s,0))
    while queue:
        now, dis = queue.popleft()
        if dis == K:
            answer.append(now)
            continue
        for next in graph[now]:
            if not visited[next]:
                queue.append((next,dis+1))
                visited[next] = 1

bfs(X)
if answer:
    print(*sorted(answer), sep='\n')
else:
    print(-1)