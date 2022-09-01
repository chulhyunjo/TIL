from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int,input().rstrip().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(n)]
queue = deque()
result = 0
maxV = 0
for i in range(n):
    for j in range(m):
        cnt = 0
        if graph[i][j] == 1:
            queue.append((i,j))
            result += 1
            cnt += 1

        while queue:
            x, y = queue.popleft()
            graph[x][y] = 0
            for q in range(4):
                nx = x + dx[q]
                ny = y + dy[q]

                if 0 > nx or n <= nx or 0 > ny or m <= ny:
                    continue
                if graph[nx][ny] == 0:
                    continue
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
        maxV = max(maxV, cnt)

print(result, maxV, sep='\n')