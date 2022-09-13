import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)    # 재귀 limit 늘리기
dx = [0, 0, 1, -1]              # dx, dy 선언
dy = [1, -1, 0 ,0]

def dfs(x,y):                   # dfs 선언
    global cnt                  # 음식물의 크기를 담을 변수
    graph[x][y] = 0             # 현재 지역 방문
    for q in range(4):
        nx = x + dx[q]          # 다음 좌표 nx, ny
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                cnt += 1        # 다음 좌표갔으면 음식물의 크기 1증가
                dfs(nx,ny)      # 다음 좌표 dfs


n, m, k = map(int,input().split())  # n: 세로, m: 가로, k: 음식물 개수
graph = [[0] * m for _ in range(n)] # 음식물 2중 배열
for _ in range(k):                  # k개의 음식물 좌표
    a, b = map(int,input().rstrip().split())
    graph[a-1][b-1] = 1             # 음식물 표시
result = 0                          # 결과값
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:        # 1이면 음식물 크기 탐색
            cnt = 1                 # cnt초기값 1로 설정
            dfs(i,j)
            result = max(cnt, result)   # 음식물의 크기 최대값을 result에 담기
print(result)