"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

3
"""
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
visit[x][y] = 1

def turn_left():
    global direction
    direction -= 1
    if direction == -1: direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx, ny = x + dx[direction], y + dy[direction]

    if graph[nx][ny] == 0 and visit[nx][ny] == 0:
        graph[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nx, ny = x - dx[direction], y - dy[direction]

        if graph[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        else:
            break

print(count)