from collections import deque
INF = 100001

def bfs():
    while queue:
        now = queue.popleft()
        if now == K:
            return
        if now + 1 < 100001 and visited[now] + 1 < visited[now+1]:
            visited[now+1] = visited[now]+1
            queue.append(now+1)

        if now - 1 >= 0 and visited[now] + 1 < visited[now-1]:
            visited[now-1] = visited[now] + 1
            queue.append(now-1)

        if 2 * now < 100001 and visited[now] < visited[2*now]:
            visited[2*now] = visited[now]
            queue.appendleft(2*now)

N, K = map(int,input().split())
queue = deque([N])
visited = [INF] * 100001
visited[N] = 0
bfs()
print(visited[K])