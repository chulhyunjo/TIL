from collections import deque
isInGraph = lambda x, y : 0 <= x < N and 0 <= y < N
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def checkTime(virusArr):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    for x,y in virusArr:
        queue.append((x,y,0))
        visited[x][y] = True
    room = 0
    while queue:
        x, y, time = queue.popleft()
        if time >= answer:
            return answer

        for q in range(4):
            nx, ny = x + dx[q], y + dy[q]
            if not isInGraph(nx,ny) or visited[nx][ny]: continue
            if graph[nx][ny] == 1: continue
            if graph[nx][ny] == 0:
                room += 1
                if room == nums:
                    return time + 1
            visited[nx][ny] = True
            queue.append((nx,ny,time+1))
    return 5000

def makeVirus(d,virusArr):
    global answer
    if len(virusArr) == M:
        time = checkTime(virusArr)
        answer = min(time,answer)
        return

    for i in range(d, virusNums):
        makeVirus(i+1, virusArr + [virus[i]])


N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

nums = 0
virusNums = 0
virus = []
answer = 5000
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i,j))
            virusNums += 1
        elif graph[i][j] == 0:
            nums += 1
if nums == 0:
    print(0)
else:
    makeVirus(0, [])
    print(answer if answer != 5000 else -1)