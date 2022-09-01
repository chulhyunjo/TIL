import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x,y):
    global result
    graph[x][y] = 1
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                dfs(nx,ny)

        if nx >= n:
            result = 1


n, m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
result = 0
for i in range(m):
    if graph[0][i] == 0:
        dfs(0,i)
    if result:
        break

if result: print("YES")
else: print("NO")