dx = [0,0,1,-1]             # 상, 하, 좌, 우
dy = [1,-1,0,0]

def dfs(x,y):               # dfs 선언
    if maze[x][y] == 3:     # 3일 경우 True return
        return True
    else:
        maze[x][y] = 1      # 현재 자리 지나갔다고 표시
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1:   # 범위 안이고 지나가지 않은 자리
                if dfs(nx,ny):  # 최종 목적지 3을 방문 하면 return True
                    return True
        return False            # 아닐 경우 False


for tc in range(1, int(input())+1):
    n = int(input())
    maze = [list(map(int,input())) for _ in range(n)]
    result = 0                  # 최종 결과 : 3을 가면 '1' 아니면 '0'

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2: # 출발지 '2'를 찾기
                if dfs(i,j):    # '2'에서 탐색 시작
                    result = 1  # 도착지에 갈 수 있는 경우 result = 1
    print(f'#{tc} {result}')