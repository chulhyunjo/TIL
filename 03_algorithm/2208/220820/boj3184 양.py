import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]


def dfs(x, y):
    global count_wolf
    global count_sheep
    visited[x][y] = True
    if graph[x][y] == 'v':
        count_wolf += 1
    if graph[x][y] == 'o':
        count_sheep += 1

    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]

        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            continue
        if visited[nx][ny] or graph[nx][ny] == '#':
            continue
        else:
            dfs(nx, ny)


w = s = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] in ['.', 'v', 'o'] and not visited[i][j]:
            count_sheep = 0
            count_wolf = 0
            dfs(i, j)
            if count_sheep > count_wolf:
                s += count_sheep
            else:
                w += count_wolf

print(s, w)
