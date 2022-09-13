from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs를 이용해서 최단 거리를 구한다
def bfs(x,y, cnt):
    queue = deque()
    queue.append((x,y, cnt))
    visited[x][y] = True
    while queue:
        x, y, cnt = queue.popleft()
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = True
    return cnt

n, m = map(int,input().rstrip().split())    # n: 세로 길이, m: 가로 길이
graph = [list(input().rstrip()) for _ in range(n)]
maxV = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':  # 현재 위치가 땅인 경우
            visited = [[False] * m for _ in range(n)]
            depth = bfs(i,j,0)  # bfs를 통해 현재 위치에서 가장 먼 곳을 찾는다
            maxV = max(maxV, depth) # maxV에 최대 길이 담기
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.