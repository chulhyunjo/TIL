from collections import deque
D = [(0,1),(1,0),(0,-1),(-1,0)]

snake = deque([(1,1)])
d = 0       # 오른쪽

N = int(input())    # 보드 크기
K = int(input())    # 사과 개수
graph = [[0] * (N+2) for _ in range(N+2)]
graph[1][1] = 2

# 벽 세우기
for i in range(N):
    graph[i][0] = -1
    graph[i][N+1] = -1
    graph[0][i] = -1
    graph[N+1][i] = -1

for _ in range(K):
    a, b = map(int,input().split())
    graph[a][b] = 1

L = int(input())
directions = deque([input().split() for _ in range(L)])

time = 0
while True:
    time += 1
    x, y = snake[0]
    dx, dy = D[d]
    nx, ny = x + dx, y + dy

    # 벽, 몸이면 게임 끝
    if graph[nx][ny] == -1 or graph[nx][ny] == 2:
        break

    # 머리 부분 확장
    snake.appendleft((nx,ny))

    # 사과 없으면 꼬리 줄어듬
    if graph[nx][ny] == 0:
        a, b = snake.pop()
        graph[a][b] = 0

    # 머리 부분도 2로 변경
    graph[nx][ny] = 2

    # 회전 시간
    if directions and time == int(directions[0][0]):
        t, nd = directions.popleft()
        if nd == 'L':
            d = (d+3) % 4
        else:
            d = (d+1) % 4

print(time)