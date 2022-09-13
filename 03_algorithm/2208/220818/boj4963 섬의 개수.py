from collections import deque
import sys
input = sys.stdin.readline


def bfs(x,y):
    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,1,-1,1,-1]
    queue = deque()
    queue.append([x,y])
    while queue:
        v = queue.popleft()
        for q in range(8):
            nx = v[0] + dx[q]
            ny = v[1] + dy[q]
            if 0 > nx or h <= nx or 0 > ny or w <= ny:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])

    return 1


while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                graph[i][j] = 0
                result += bfs(i,j)

    print(result)