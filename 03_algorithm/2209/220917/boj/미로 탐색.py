from collections import deque
n, m  = map(int,input().split())    # 미로의 크기 nxm
graph = [list(map(int,input())) for _ in range(n)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
# bfs
queue = deque()
queue.append((0,0))
while queue:
    x, y = queue.popleft()          # (x, y)현재 탐색 위치
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0<= ny < m and graph[nx][ny] == 1:   # 다음 이동할 수 있는 칸인지 확인
            graph[nx][ny] = graph[x][y] + 1 # 이동한 칸은 현재 위치 + 1
            queue.append((nx,ny))           # 다음 이동위치 queue에 담기
print(graph[n-1][m-1])                      # (n,m)위치에 가기 위한 이동 횟수 프린트