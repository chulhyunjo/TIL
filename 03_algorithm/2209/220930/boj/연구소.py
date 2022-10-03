dx, dy = [0,0,1,-1], [1,-1,0,0]
def bfs(n2):
    queue = []
    for x, y in n2:
        queue.append((x,y))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    idx = 0
    q_len = len(queue)
    while idx < q_len:
        x,y = queue[idx][0], queue[idx][1]
        for q in range(4):
            nx, ny = x + dx[q], y + dy[q]
            if 0 > nx or n <= nx or 0 > ny or m <= ny: continue
            if not visited[nx][ny] and not graph[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                q_len +=1
        idx += 1
    return q_len

def makeWall(d,b):
    global maxV
    if d == 3:
        result = b - bfs(num2) + len(num2) - 3
        if result > maxV: maxV = result
    else:
        for x,y in num0:
            if graph[x][y] == 0:
                graph[x][y] = 1
                makeWall(d+1, b)
                graph[x][y] = 0


n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
maxV = 0
num2 = []
num0 = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            num2.append((i,j))
        elif graph[i][j] == 0:
            num0.append((i,j))
Blank = len(num0)
makeWall(0,Blank)
print(maxV)