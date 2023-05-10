from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

times = [[0]*(N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
reverseGraph = [[] for _ in range(N+1)]
info = [0] * (N+1)

for _ in range(M):
    a, b, t = map(int,input().rstrip().split())
    graph[a].append(b)
    reverseGraph[b].append(a)
    times[a][b] = t
    times[b][a] = t
    info[b] += 1

queue = deque()
endPoint = 0

for i in range(1, N+1):
    # 시작 지점
    if info[i] == 0:
        queue.append(i)
    if not graph[i]:
        endPoint = i

time = [0] * (N+1)
while queue:
    now = queue.popleft()
    for next in graph[now]:
        info[next] -= 1
        time[next] = max(time[next], time[now]+times[now][next])
        if info[next] == 0:
            queue.append(next)

resultTime = time[endPoint]
visited = [False] * (N+1)
queue.append(endPoint)
resultCnt = 0
visited[endPoint] = True
while queue:
    now = queue.popleft()
    for next in reverseGraph[now]:
        if time[next] + times[next][now] == time[now]:
            resultCnt += 1
            if not visited[next]:
                visited[next] = True
                queue.append(next)

print(resultTime)
print(resultCnt)