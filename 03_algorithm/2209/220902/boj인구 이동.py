from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x,y):
    global sum1             # 이동할 인구수를 담을 변수
    global change_yn        # 이동 여부
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    change.append((x,y))
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if 0 <= nx < n and 0 <= ny < n: # 그래프 안이고 두 나라의 차이가 L이상 R이하이면 실행
                if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True  # 현재 지점을 방문
                    queue.append((nx,ny))   # bfs에 담기
                    change.append((nx,ny))  # 현재 위치를 change 리스트에 담기
                    sum1 += graph[nx][ny]   # 이동할 인구의 총수에 더하기
                    change_yn = 1           # 이동 여부 True

n , l, r = map(int,input().split())     # n : 배열의 크기, 두 나라의 인구 차이는 L명 이상 R명 이하 기준
graph = [list(map(int,input().split())) for _ in range(n)]
time = 0                                # 이동이 며칠 동안 발생한지 담을 변수
while True:
    change_yn = 0                       # 오늘 중에 변화가 있었는지 없었는지 확인할 변수
    visited = [[False] * n for _ in range(n)]   # visited
    for i in range(n):                  # 전체 탐색
        for j in range(n):
            if not visited[i][j]:       # 방문하지 않았을 경우
                sum1 = graph[i][j]      # 이동할 인구수를 담을 변수 선언
                change = []             # 이동할 나라의 위치를 담을 리스트
                bfs(i,j)                # bfs
            avg = sum1 // len(change)   # 평균 구하기
            for x, y in change:         # 인구 이동이 있는 나라들을 평균값으로 교체
                graph[x][y] = avg
    if not change_yn:                   # 오늘 중 이동이 없다면 break
        break
    time += 1                           # 있었다면 1일 추가

print(time)