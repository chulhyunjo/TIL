dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    global cnt              # 단지 내의 집 수를 담을 변수
    cnt += 1                # 집의 개수 + 1
    graph[x][y] = 0         # 현재 집을 방문 표시
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
                            # 다음 좌표가 범위 내에 있고 집인 경우 다음 좌표 dfs 실행
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx,ny)


n = int(input())            # n: 지도의 크기
graph = [list(map(int,input())) for _ in range(n)]
result = []                 # 단지 내의 집의 수를 담을 리스트
for i in range(n):          # NxN 크기의 배열을 탐색
    for j in range(n):
        if graph[i][j] == 1: # 현재 좌표가 '1: 집'인 경우
            cnt = 0         # 단지 내 집의 개수를 담을 변수 선언
            dfs(i,j)        # dfs 실행
            result.append(cnt)  # 단지 내 집의 개수를 리스트에 담기
# 출력하기
print(len(result))          # 현재 지도내의 단지 개수
for i in sorted(result):    # 각 단지내의 집의 개수를 오름 차순
    print(i)