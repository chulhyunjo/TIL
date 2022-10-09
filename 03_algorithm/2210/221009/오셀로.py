for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    graph = [[0]*n for _ in range(n)]
    graph[n//2-1][n//2-1] = graph[n//2][n//2] = 2
    graph[n//2][n//2-1] = graph[n//2-1][n//2] = 1
    for _ in range(m):
        x, y, c = map(int,input().split())
        graph[x-1][y-1] = c
        f_change = []
        for dx, dy in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
            find = 0
            change = []
            nx, ny = (x-1)+dx, (y-1)+dy
            while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 0 :
                if graph[nx][ny] == c:
                    find = 1
                    break
                change.append((nx,ny))
                nx, ny = nx+dx, ny+dy
            if find:
                f_change.append(change)
        for i in f_change:
            for x, y in i:
                graph[x][y] = c
    result_w = 0
    result_b = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                result_b += 1
            elif graph[i][j] == 2:
                result_w += 1
    print(f'#{tc} {result_b} {result_w}')