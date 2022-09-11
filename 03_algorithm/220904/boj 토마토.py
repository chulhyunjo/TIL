from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0 ,0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# m : 가로 길이, n : 세로 길이, h : 높이
m, n, h = map(int,input().rstrip().split())
# 토마토 상자 배열
graph = [[list(map(int,input().rstrip().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
need = 0    # 익지 않은 토마토의 수를 담을 변수
for k in range(0, h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                need += 1   # 익지 않은 토마토의 수 +1
            if graph[k][i][j] == 1:
                queue.append((k, i, j, 0))  # 익은 토마토의 위치 담기, 0 : 걸린 날(현재=0)

while queue:
    for _ in range(len(queue)):
        k, x, y, cnt = queue.popleft()
        for q in range(6):
            nx = x + dx[q]
            ny = y + dy[q]
            nz = k + dz[q]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    queue.append((nz,nx,ny,cnt +1))
                    graph[nz][nx][ny] = 1
                    need -= 1       # 익지 않음 토마토의 수 -1
if need:        # 익지 않은 토마토가 아직 있다면 -1
    print(-1)
else:           # 없는 경우 걸린 날 출력
    print(cnt)