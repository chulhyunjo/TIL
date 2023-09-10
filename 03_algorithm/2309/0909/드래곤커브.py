N = int(input())
direction = [(0,1), (-1,0), (0,-1), (1,0)]
graph = [[0] * 101 for _ in range(101)]
#3
# 3 3 0 1
# 4 2 1 3
# 4 2 2 1

# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
for i in range(1, N+1):
    x, y, d, g = map(int,input().split())
    graph[y][x] = i
    now_g = 0

    # 처음 0세대
    dy, dx = direction[d]
    ny, nx = y + dy, x + dx
    graph[ny][nx] = i
    y, x = ny, nx
    move = [d]
    while now_g < g:
        mm = list(map(lambda x: (int(x)+1)%4, reversed(move)))
        nxt_move = []
        for m in mm:
            dy, dx = direction[m]
            ny, nx = y + dy, x + dx
            graph[ny][nx] = i
            nxt_move.append(m)
            y, x = ny, nx
        move += nxt_move
        now_g += 1
answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j+1] and graph[i+1][j] and graph[i][j+1]:
            answer += 1
print(answer)