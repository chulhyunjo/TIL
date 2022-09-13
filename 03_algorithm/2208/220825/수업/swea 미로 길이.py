dx = [0, 1, 0, -1]                                  # 상하 좌우
dy = [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    n = int(input())                                # 미로 크기
    maze = [list(map(int, input())) for _ in range(n)]   # 미로
    move = []                                       # bfs 이동 경로
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                move.append((i,j))                  # bfs경로에 추가
                maze[i][j] = 0                      # 시작점을 0으로 초기화
            if maze[i][j] == 3:
                maze[i][j] = 'x'                    # 도착지점을 x로 초기화
    result = 0                                      # 결과값을 담을 변수
    while move:                                     # 움직일 공간 있을 때 까지
        x, y = move.pop(0)                          # 첫 시작점을 x, y에 담기
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if 0 > nx or n <= nx or 0 > ny or n <= ny:
                continue
            if maze[nx][ny] == 0:                   # 이동할 수 있는 칸이면
                maze[nx][ny] = maze[x][y] + 1       # 전 칸의 이동 횟수 + 1
                move.append((nx, ny))                # 다음칸으로 이동
            if maze[nx][ny] == 'x':                 # 도착지점
                result = maze[x][y]                 # 전 단계의 이동 횟수를 result에 담기
        if result:
            break

    print(f'#{tc} {result}')