from collections import deque

isInGraph = lambda x, y : 0 <= x < 12 and 0 <= y < 6
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def changeGraph():
    for i in range(10,-1,-1):
        for j in range(6):
            if graph[i][j] != '.' and graph[i+1][j] == '.':
                k = 1
                while i+k < 12 and graph[i+k][j] == '.':
                    graph[i+k][j] = graph[i+(k-1)][j]
                    graph[i+(k-1)][j] = '.'
                    k += 1

def bfs(x,y, color):
    queue = deque()
    queue.append((x,y,0))
    visited[x][y] = True
    position = [(x,y)]
    while queue:
        x, y, cnt = queue.popleft()
        for m in range(4):
            nx, ny = x+dx[m], y+dy[m]
            if not isInGraph(nx,ny): continue
            if visited[nx][ny] or color != graph[nx][ny]: continue
            queue.append((nx,ny,cnt+1))
            visited[nx][ny] = True
            position.append((nx,ny))
    if len(position) >= 4:
        for x,y in position:
            graph[x][y] = '.'
        return True
    else:
        return False

graph = [list(input()) for _ in range(12)]
answer = 0
while True:
    flag = 0
    visited = [[False] * 6 for _ in range(12)]
    for i in range(11,-1,-1):
        for j in range(6):
            if not visited[i][j] and graph[i][j] != '.':
                isTrue = bfs(i,j,graph[i][j])
                if isTrue:
                    flag = 1
    if flag:
        answer += 1
        changeGraph()
    else:
        break
print(answer)