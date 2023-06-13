from collections import deque
dx, dy = [0,0,1,-1], [1,-1,0,0]
horse = [(-1,-2), (-2,-1),(-2,1),(-1,2), (1,2), (1,-2), (2,-1), (2,1)]

K = int(input())
W, H = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(H)]

queue = deque([(0, 0, 0)])
visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1

answer = -1
while queue:
    x, y, z = queue.popleft()
    if x == H-1 and y == W-1:
        answer = visited[x][y][z] - 1
        break
    for m in range(4):
        nx, ny = x + dx[m], y +dy[m]
        if 0>nx or H<= nx or 0>ny or W<=ny: continue
        if visited[nx][ny][z] or graph[nx][ny] == 1 : continue
        queue.append((nx,ny,z))
        visited[nx][ny][z] = visited[x][y][z] + 1
    if z < K:
        for mx, my in horse:
            nx, ny = x+mx, y+my
            if 0>nx or H<= nx or 0>ny or W<=ny: continue
            if graph[nx][ny] == 1 or visited[nx][ny][z+1]: continue
            visited[nx][ny][z+1] = visited[x][y][z] + 1
            queue.append((nx,ny,z+1))
print(answer)