dx, dy = [0,1,0,-1], [1,0,-1,0]
for tc in range(1,int(input())+1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    now = 1
    x = y = move =0
    while True:
        graph[x][y] = now
        nx, ny = x + dx[move], y + dy[move]
        if nx<0 or ny<0 or nx>=n or ny>=n or graph[nx][ny] != 0:
            move = (move+1) % 4
            nx = x + dx[move]
            ny = y + dy[move]
        x,y = nx, ny
        now += 1

        if now > n**2:
            break
    print(f'#{tc}')
    for line in graph:
        print(*line)