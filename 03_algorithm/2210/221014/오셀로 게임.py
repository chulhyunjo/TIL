for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    graph = [[0]*n for _ in range(n)]
    graph[n//2][n//2] = graph[n//2-1][n//2-1] = 2
    graph[n//2-1][n//2] = graph[n//2][n//2-1] = 1
    for _ in range(m):
        x, y, c = map(int,input().split())
        x -= 1
        y -= 1
        graph[x][y] = c
        change = []
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            nx = x + dx
            ny = y + dy
            find = []
            if nx<0 or nx>=n or ny<0 or ny>=n: continue
            while 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0: break
                elif graph[nx][ny] == c:
                    change.append(find)
                    break
                find.append((nx,ny))
                nx, ny = nx+dx, ny+dy
        for i in change:
            for x, y in i:
                graph[x][y] = c
    resultW = 0
    resultB = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                resultB += 1
            elif graph[i][j] == 2:
                resultW += 1
    print(f'#{tc} {resultB} {resultW}')
