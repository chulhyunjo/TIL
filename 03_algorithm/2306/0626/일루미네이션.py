from collections import deque
D = {
    'odd':[(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0)],
    'even':[(0,1),(0,-1),(-1,0),(-1,1),(1,0),(1,1)]
     }

def findOut(x, y, o_e):
    queue = deque()
    queue.append((x,y,o_e))
    visited[x][y] = 1
    tmp = 0
    history = [(x,y)]
    while queue:
        x, y, o_e = queue.popleft()
        for dx, dy in D.get(o_e):
            nx, ny = x + dx, y + dy
            if 0 >= nx or 0 >= ny or N < nx or M < ny:
                tmp = 1
                continue
            if visited[nx][ny] or graph[nx][ny] == 1: continue
            visited[nx][ny] = 1
            queue.append((nx,ny, 'odd' if nx % 2 else 'even'))
            history.append((nx,ny))
    if not tmp:
        for x, y in history:
            graph[x][y] = -1

def findArea(x, y, o_e):
    queue = deque([(x,y,o_e)])
    visited[x][y] = 1
    area = 0
    while queue:
        x, y, o_e = queue.popleft()
        cnt = 0
        for dx, dy in D.get(o_e):
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or N + 1 < nx or M < ny: continue
            if visited[nx][ny]: continue
            if graph[nx][ny] == 1:
                area += 1
            if graph[nx][ny] == 0 or graph[nx][ny] == -1:
                queue.append((nx,ny,'odd' if nx % 2 else 'even'))
                visited[nx][ny] = 1

    return area

M, N = map(int,input().split())
graph = [[0] *(M+1)]
for i in range(N):
    if not i % 2:
        graph.append([-1] + list(map(int,input().split())) + [0])
    else:
        graph.append([0]+list(map(int,input().split())) + [-1])
graph.append([0] * (M+1))

visited = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(M+1):
        if graph[i][j] == 0 and not visited[i][j]:
            if not i % 2:
                findOut(i, j, 'odd')
            else:
                findOut(i, j, 'even')

visited = [[0]*(M+1) for _ in range(N+2)]
answer = 0
for i in range(N+2):
    for j in range(M+1):
        if graph[i][j] == 0 and not visited[i][j]:
            answer += findArea(i,j,'odd' if i%2 else 'even')
print(answer)