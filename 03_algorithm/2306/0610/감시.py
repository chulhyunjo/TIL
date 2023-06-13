dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
isInGraph = lambda x, y: 0 <= x < N and 0 <= y < M

def changeGraph(nx, ny, m, number):
    global nums
    while True:
        nx, ny = nx + dx[m], ny + dy[m]
        if not isInGraph(nx, ny): break
        if graph[nx][ny] == 0:
            graph[nx][ny] = number
            nums -= 1
        if graph[nx][ny] == 6:
            break

def returnGraph(nx, ny, m, number):
    global nums
    while True:
        nx, ny = nx + dx[m], ny + dy[m]
        if not isInGraph(nx, ny): break
        if graph[nx][ny] == number:
            graph[nx][ny] = 0
            nums += 1
        if graph[nx][ny] == 6:
            break

def check(d):
    global nums, answer
    if d == cctv_nums:
        answer = min(nums, answer)
        return
    x, y, cctvnumber = cctvs[d]
    if cctvnumber == 1:
        for move in range(4):
            changeGraph(x, y, move, d+64)
            check(d+1)
            returnGraph(x, y, move, d+64)

    if cctvnumber == 2:
        for move in range(2):
            changeGraph(x, y, move, d+64)
            changeGraph(x, y, (move + 2) % 4,d+64)
            check(d+1)
            returnGraph(x, y, move, d+64)
            returnGraph(x, y, (move + 2) % 4, d+64)

    if cctvnumber == 3:
        for move in range(4):
            changeGraph(x, y, move, d+64)
            changeGraph(x, y, (move + 1) % 4, d+64)
            check(d+1)
            returnGraph(x, y, move, d+64)
            returnGraph(x, y, (move + 1) % 4, d+64)

    if cctvnumber == 4:
        for move in range(4):
            changeGraph(x, y, move, d+64)
            changeGraph(x, y, (move + 1) % 4, d+64)
            changeGraph(x, y, (move + 2) % 4, d+64)
            check(d+1)
            returnGraph(x, y, move, d+64)
            returnGraph(x, y, (move + 1) % 4, d+64)
            returnGraph(x, y, (move + 2) % 4, d+64)

    if cctvnumber == 5:
        changeGraph(x, y, 0, 5)
        changeGraph(x, y, 1, 5)
        changeGraph(x, y, 2, 5)
        changeGraph(x, y, 3, 5)
        check(d+1)
        returnGraph(x, y, 0, 5)
        returnGraph(x, y, 1, 5)
        returnGraph(x, y, 2, 5)
        returnGraph(x, y, 3, 5)



def cctv5(nx, ny, m):
    changeGraph(nx, ny, m)
    changeGraph(nx, ny, (m + 1)%4)
    changeGraph(nx, ny, (m + 2)%4)
    changeGraph(nx, ny, (m + 3)%4)



N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

nums = 0
cctvs = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            nums += 1
        if 1 <= graph[i][j] <= 5:
            cctvs.append((i, j, graph[i][j]))

answer = nums
cctv_nums = len(cctvs)
check(0)
print(answer)