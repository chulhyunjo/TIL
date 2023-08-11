from collections import deque
import sys
input = sys.stdin.readline

# 0: 오른쪽, 1: 위쪽, 2: 왼쪽, 3: 아래
sign = {
    1:[(0, 0, 1, 0), (0, -1, 0, 1), (0, 1, 0, 3)], 2:[(1, -1, 0, 1), (1, 0, -1, 2), (1, 0, 1, 0)],
    3:[(2, -1, 0, 1), (2, 0, -1, 2), (2, 1, 0, 3)], 4: [(3, 1, 0, 3), (3, 0, -1, 2), (3, 0, 1, 0)],
    5:[(0, 0, 1, 0), (0, -1, 0, 1)], 6: [(1, -1, 0, 1), (1, 0, -1, 2)], 7: [(2, 0, -1, 2), (2, 1, 0, 3)],
    8: [(3, 1, 0, 3), (3, 0, 1, 0)], 9: [(0, 0, 1, 0), (0, 1, 0, 3)], 10:[(1, -1, 0, 1), (1, 0, 1, 0)],
    11: [(2, 0, -1, 2), (2, -1, 0, 1)], 12: [(3, 1, 0, 3), (3, 0, -1, 2)]
}

N, T = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(N)]

queue = deque()
answer = 1
x = y = 0
queue.append((1, x, y, 0))
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1

while queue:
    d, x, y, time = queue.popleft()
    if time >= T: break

    info = sign[graph[x][y][time%4]]
    if d != info[0][0]: continue
    for dr, dx, dy, nxtdr in info:
        nx, ny = x + dx, y + dy
        if 0 > nx or N <= nx or 0 > ny or N <= ny: continue
        queue.append((nxtdr, nx, ny, time + 1))
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            answer += 1

print(answer)