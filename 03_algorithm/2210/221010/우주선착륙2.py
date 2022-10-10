for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            look = 0
            now = graph[i][j]
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,1),(-1,-1)]:
                nx, ny = i+dx, j+dy
                if 0 > nx or n <= nx or 0 > ny or m <= ny: continue
                if now > graph[nx][ny]: look += 1
            if look >= 4: result += 1

    print(f'#{tc} {result}')