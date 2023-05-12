import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
dx, dy = [0,0,1,-1], [1,-1,0,0]

num = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int,input().rstrip().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = graph[0][0]

    pq = []
    heapq.heappush(pq, (distance[0][0], 0, 0))

    while pq:
        dis, x, y = heapq.heappop(pq)
        if x == N-1 and y == N-1:
            print('Problem %d: %d' %(num, dis))
            break
        if dis > distance[x][y]: continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if distance[nx][ny] > distance[x][y] + graph[nx][ny]:
                distance[nx][ny] = distance[x][y] + graph[nx][ny]
                heapq.heappush(pq, (distance[nx][ny],nx, ny))

    num += 1