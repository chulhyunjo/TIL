import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global cnt
    graph[x][y] = 1
    cnt += 1
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            dfs(nx, ny)


m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

area_list = []
for q in range(m):
    for w in range(n):
        if graph[q][w] == 0:
            cnt = 0
            dfs(q, w)
            area_list.append(cnt)

print(len(area_list))
print(*sorted(area_list))
