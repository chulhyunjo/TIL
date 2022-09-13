import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [0, -1, 1]
dy = [1, 0, 0]


def dfs(x, y, i, tec):
    global result
    if i == 4:
        result = max(result, tec)
        return
    else:
        for q in range(3):
            nx = x + dx[q]
            ny = y + dy[q]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, i+1, tec+graph[nx][ny])
                visited[nx][ny] = False


def T_sum1(x, y, i, tec):
    global result
    if i == 3:
        move = [1, -1]
        for a in move:
            tmp = tec
            ny = y + a
            if 0 <= ny < m:
                tmp += graph[x-1][ny]
                result = max(result, tmp)
        return
    else:
        nx = x + 1
        if 0 <= nx < n:
            T_sum1(nx ,y, i+1, tec + graph[nx][y])

def T_sum2(x, y, i, tec):
    global result
    if i == 3:
        move = [1, -1]
        for a in move:
            tmp = tec
            nx = x + a
            if 0 <= nx < n:
                tmp += graph[nx][y-1]
                result = max(result, tmp)
        return
    else:
        ny = y + 1
        if 0 <= ny < m:
            T_sum2(x ,ny, i+1, tec + graph[x][ny])


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False
        T_sum1(i, j, 1, graph[i][j])
        T_sum2(i, j, 1, graph[i][j])
print(result)