dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y):
    if graph[x][y] == 3:
        return 1
    else:
        graph[x][y] = 1
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1:
                if dfs(nx,ny):
                    return 1
        return 0


for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int,input())) for _ in range(n)]

    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                if dfs(i,j):
                    result = 1

    print(f'#{tc} {result}')