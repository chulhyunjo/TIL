from collections import deque
import sys
input = sys.stdin.readline

def check_move(x, y, dx, dy):
    if dy == 1:
        for i in range(x, x+H+1):
            if graph[i][y+W]: return False
    elif dy == -1:
        for i in range(x, x+H+1):
            if graph[i][y]: return False
    elif dx == 1:
        for i in range(y, y+W+1):
            if graph[x+H][i]: return False
    elif dx == -1:
        for i in range(y, y+W+1):
            if graph[x][i]: return False
    return True

def bfs():
    queue = deque([(s1, s2, 0)])
    visited[s1][s2] = 1
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or N <= nx or M <= ny or N <= nx + H or M <= ny + W: continue
            if visited[nx][ny]: continue
            if check_move(nx, ny, dx, dy):
                if nx == f1 and ny == f2:
                    return cnt + 1
                queue.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1
    return -1


N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
H, W, s1, s2, f1, f2 = map(lambda x: int(x) - 1, input().split())
visited = [[0] * M for _ in range(N)]

print(bfs())