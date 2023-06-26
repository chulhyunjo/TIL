import heapq

R, C, N = map(int,input().split())
graph = [list(input()) for _ in range(R)]
timeGraph = [[-1] * C for _ in range(R)]

pq = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'O':
            heapq.heappush(pq, (0,i,j))
            timeGraph[i][j] = 0

time = 1
tmp = 1
while time < N:
    time += 1
    if tmp:
        for i in range(R):
            for j in range(C):
                if graph[i][j] == '.':
                    graph[i][j] = 'O'
                    timeGraph[i][j] = time
                    heapq.heappush(pq, (time,i,j))
                else:
                    heapq.heappush(pq, (timeGraph[i][j],i,j))

        tmp = 0
    while pq and time - pq[0][0] >= 3:
        t, x, y = heapq.heappop(pq)
        graph[x][y] = '.'
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or R <= nx or C <= ny: continue
            graph[nx][ny] = '.'
            timeGraph[nx][ny] = time + 1
            tmp = 1
    if tmp:
        pq = []

for i in range(R):
    print(*graph[i], sep='')