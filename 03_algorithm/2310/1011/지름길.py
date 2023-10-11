from collections import deque

N, D = map(int,input().split())
lines = dict()
for _ in range(N):
    a, b, l = map(int,input().split())
    lines[a] = lines.get(a,[]) + [(b, l)]

visited = [10001] * (D+1)

queue = deque([0])
visited[0] = 0
while queue:
    now = queue.popleft()
    if lines.get(now, 0):
        for nx, l in lines[now]:
            if nx <= D and visited[now] + l < visited[nx]:
                visited[nx] = visited[now] + l
                queue.append(nx)
    if now + 1 <= D and visited[now] + 1 < visited[now+1]:
        visited[now+1] = visited[now] + 1
        queue.append(now+1)
print(visited[D])