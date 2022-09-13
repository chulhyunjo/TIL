import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x,y):
    global result           # 최종 결과값
    graph[x][y] = 1         # 현재 위치 방문
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                dfs(nx,ny)

        if nx >= n:         # 만약 아래로 벗어나면 전류가 전달되는 것
            result = 1


n, m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
result = 0
for i in range(m):
    if graph[0][i] == 0:    # 전류가 잘통하는 곳이면 dfs탐색
        dfs(0,i)
    if result:              # 결과가 나왔다면 break
        break

if result: print("YES")     # 전류가 흐르면 YES 아니면 NO
else: print("NO")