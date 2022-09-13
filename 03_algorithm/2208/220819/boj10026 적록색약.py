import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(input()) for _ in range(n)]
visited_nc = [[False] * n for _ in range(n)] # 적약색약 x
visited_yc = [[False] * n for _ in range(n)] # 적약색약 o
def dfs(x, y, visit_list):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit_list[x][y] = True
    color = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visit_list[nx][ny] and graph[nx][ny] == color:
            dfs(nx,ny,visit_list)


no_color = 0 # 적약x
yes_color = 0 # 적약 o
for i in range(n):
    for j in range(n):
        if not visited_nc[i][j]:
            dfs(i,j,visited_nc)
            no_color += 1

# 적록색약 그래프 만들기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited_yc[i][j]:
            dfs(i,j,visited_yc)
            yes_color += 1

print(no_color, yes_color)