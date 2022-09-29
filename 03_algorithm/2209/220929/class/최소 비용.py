dx, dy = [1,-1,0,0], [0,0,1,-1]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    q = [(0,0)]
    maxV = 100000
    result = [maxV] * (n**2)
    result[0] = 0
    idx = 0
    while q:
        x, y = q.pop(0)
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0 > nx or 0 > ny or n <= nx or n <= ny:
                continue
            if graph[nx][ny] > graph[x][y]:
                price = 1 + graph[nx][ny] - graph[x][y]
            else:
                price = 1
            if result[x*n + y] + price >= result[nx* n +ny]:
                continue
            else:
                result[nx*n + ny] = result[x*n + y] + price
                q.append((nx,ny))
    print(f'#{tc} {result[(n-1)* n + (n-1)]}')