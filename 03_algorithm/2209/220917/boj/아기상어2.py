from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
eat = 0     # 현재까지 먹은 물고기 수를 담을 변수
result = 0  # 결과값(이동한 시간)을 담을 변수
size = 2    # 현재 아기 상어의 크기 (초기값:2)

n = int(input())    # nxn 배열
graph = []          # 그래프 리스트 생성
for i in range(n):
    l = list(map(int, input().split())) # 1줄씩 입력 받는다
    graph.append(l)                     # 그래프에 append
    for j in range(n):
        if l[j] == 9:                   # 현재 줄에 9가 있다면
            start_x, start_y = i, j     # 9의 위치를 저장한다


while True:         # 상어가 이동할 수 있는 동안 진행
    end_shark = 1   # 상어의 이동을 확인할 변수 선언 ( 1: 이동x, 0: 이동o )
    eat_time = 400  # 먹이 먹으러 걸린 시간을 담을 변수 (최대 20x20배열이므로 400으로 초기값 설정)
    move_x = move_y = 400  # 먹이의 위치를 담을 (x,y) 변수 선언
    if eat == size: # 상어의 크기 만큼 먹었다면 size += 1이 된다.
        if size > 7: size = 7   # 먹이의 최대 크기는 6이므로 max_size = 7로 설정
        size += 1               # 설정하지 않으면 나중에 상어의 크기 9가 먹이로 인식되어 무한루프..
        eat = 0     # 먹은 물고기 수를 0으로 초기화
    queue = deque()
    queue.append((start_x, start_y, 0)) # 현재 상어의 위치를 큐에 담기
    visited = [False] * (n**2)          # 방문 리스트 생성
    visited[start_x*n + start_y] = True # 상어 초기 위치 방문 설정
    while queue:
        x, y, time = queue.popleft()
        if time > eat_time: break       # 먹이까지의 최소 거리만 이동하기 위한 break
        if 0 < graph[x][y] < size:      # 현재 자리의 물고기가 상어 크기 보다 작을 경우
            if x < move_x:              # 위치가 다음 이동 위치보다 위일 경우
                move_x, move_y = x, y   # 위치값을 바꾼다
                eat_time = time         # 최소 시간을 변경
                end_shark = 0           # 상어가 이동한다고 표시 (while문 벗어나지 않기 위해)
            if x == move_x and y < move_y:  # 위치가 같은 높이지만 왼쪽일 경우
                move_x, move_y = x, y       # 먹을 먹이의 위치 변경
        for m in range(4):      # 상하 좌우 이동
            nx = x + dx[m]
            ny = y + dy[m]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx*n+ny] and graph[nx][ny]<=size:    # 상어 크기보다 크지 않으면 이동
                    queue.append((nx, ny, time + 1))
                    visited[nx*n + ny] = True
    if end_shark:   # 먹이를 찾지 못했다면 break
        break
    eat += 1        # 먹은 물고기 +1
    result += eat_time  # 결과값 += 이동 시간
    graph[start_x][start_y] = 0 # 처음 상어 위치를 0으로 초기화
    graph[move_x][move_y] = 9   # 먹은 물고기 위치를 상어 위치로 변경
    start_x, start_y = move_x, move_y   # 상어의 초기 위치 새로 담기

print(result)   # 결과값 출력