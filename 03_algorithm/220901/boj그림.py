import sys
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int,input().split()) # n: 세로, m: 가로
graph = [list(map(int,input().split())) for _ in range(n)]


def dfs(x,y):
    global cnt              # 그림의 넓이 담을 변수
    graph[x][y] = 0         # 현재 자리 방문 표시
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx,ny)
                cnt += 1    # 다음 좌표로 갈때 넓이 + 1

result = 0                  # 그림의 총 개수를 담을 변수
maxV = 0                    # 그림의 넓이 중 최대값 담을 변수
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 1                 # 현재 그림의 넓이 1로 선언
            dfs(i,j)
            result += 1             # 그림의 총 개수 + 1
            maxV = max(cnt, maxV)   # 최대값 초괴화

print(result)                       # 그림의 개수 출력
print(maxV)                         # 최대 넓이 출력