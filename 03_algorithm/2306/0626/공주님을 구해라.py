from collections import deque
D = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs():
    while queue:
        x, y, sword = queue.popleft()
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or N <= nx or M <= ny: continue
            if visited[nx][ny][sword]: continue
            if graph[nx][ny] == 1 and not sword: continue
            if graph[nx][ny] == 2:
                visited[nx][ny][1] = visited[x][y][sword] + 1
                queue.append((nx,ny,1))
            else:
                if sword:
                    if visited[nx][ny][sword] > visited[nx][ny][0]:
                        continue
                visited[nx][ny][sword] = visited[x][y][sword] + 1
                queue.append((nx,ny,sword))
            if nx == N-1 and ny == M-1:
                return visited[nx][ny][sword] - 1
            if visited[nx][ny][sword] > T+1:
                return 'Fail'
    return 'Fail'

N, M, T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)]  for _ in range(N)]

queue = deque()
queue.append((0,0,0))
visited[0][0][0] = 1

answer = bfs()
print(answer)

