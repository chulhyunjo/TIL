for tc in range(1,int(input())+1):
    n = int(input())
    graph=[list(input()) for _ in range(n)]
    result = 'NO'
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'o':
                for dx,dy in [[1,0],[0,1],[1,1],[1,-1]]:
                    nx, ny = i+dx, j+dy
                    if 0 > nx or n <= nx or 0 > ny or n <= ny or graph[nx][ny]!='o': continue
                    cnt = 1
                    while 0<=nx<n and 0<=ny<n and graph[nx][ny] == 'o':
                        cnt += 1
                        nx, ny = nx + dx, ny + dy
                    if cnt >= 5:
                        result = 'YES'
                        break
            if result == 'YES' : break
        if result == 'YES' : break
    print(f'#{tc} {result}')