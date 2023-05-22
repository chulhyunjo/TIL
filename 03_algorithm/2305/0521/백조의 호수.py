from collections import deque
isInGraph = lambda x,y : 0<=x<8 and 0<=y<8

dx, dy = [1,1,-1,-1,0,0,1,-1,0], [1,-1,1,-1,1,-1,0,0,0]
graph = [list(input()) for _ in range(8)]

startX = 7
startY=0

queue = deque()
queue.append((startX,startY))

def moveWall():
    for i in range(7,-1,-1):
        for j in range(8):
            if graph[i][j] == '#':
                nx = i + 1
                if isInGraph(nx,j):
                    graph[nx][j] = '#'
                    graph[i][j] = '.'
                else:
                    graph[i][j] = '.'


answer = 0
while queue:
    moveTurn = len(queue)
    visited = [[False] * 8 for _ in range(8)]
    for _ in range(moveTurn):
        x, y = queue.popleft()
        for m in range(9):
            nx, ny = x+dx[m], y+dy[m]
            if nx == 0 and ny == 7:
                answer = 1
                break
            if not isInGraph(nx,ny): continue
            if visited[nx][ny] or graph[nx][ny] == '#' : continue
            if nx-1 == -1 or (nx-1 >= 0 and graph[nx-1][ny] == "."):
                queue.append((nx,ny))
                visited[nx][ny] = True
        if answer: break
    if answer: break
    moveWall()

print(answer)


