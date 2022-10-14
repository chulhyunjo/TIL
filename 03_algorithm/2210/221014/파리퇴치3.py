for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            sum1 = graph[i][j]
            sum2 = graph[i][j]
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                for q in range(1,m):
                    nx, ny = i+dx*q, j+dy*q
                    if nx<0 or ny <0 or nx>=n or ny>=n: continue
                    sum1 += graph[nx][ny]
            for dx, dy in [(1,-1), (1,1), (-1,1), (-1,-1)]:
                for q in range(1,m):
                    nx, ny = i+dx*q, j+dy*q
                    if nx<0 or ny <0 or nx>=n or ny>=n: continue
                    sum2 += graph[nx][ny]
            result = max(result, sum1, sum2)
    print(f'#{tc} {result}')