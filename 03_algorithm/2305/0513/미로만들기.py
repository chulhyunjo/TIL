import heapq
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
pq = []

heapq.heappush(pq, (0,0,0))
visited[0][0] = True

while pq:
    cnt, x, y = heapq.heappop(pq)
    if x == n-1 and y == n-1:
        print(cnt)
        break
    for m in range(4):
        nx, ny = x + dx[m], y + dy[m]
        if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny]: continue
        visited[nx][ny] = True
        if graph[nx][ny] == 1:
            heapq.heappush(pq, (cnt, nx, ny))
        else:
            heapq.heappush(pq, (cnt+1, nx, ny))
