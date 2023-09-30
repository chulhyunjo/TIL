from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    global answer
    cnt = 0
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 1 > nx or 1 > ny or N < nx or N < ny: continue
            if visited[nx][ny]: continue
            if (x, y) in bridge.get((nx,ny), []):
                continue
            if cows.get((nx, ny), 0):
                cnt += 1
            queue.append((nx,ny))
            visited[nx][ny] = 1
    answer += K - cnt - 1

N, K, R = map(int, input().split())
bridge = dict()
cows = dict()

for _ in range(R):
    r1, c1, r2, c2 = map(int,input().split())
    bridge[(r1, c1)] = bridge.get((r1, c1), []) + [(r2, c2)]
    bridge[(r2, c2)] = bridge.get((r2, c2), []) + [(r1, c1)]

for _ in range(K):
    r, c = map(int,input().split())
    cows[(r,c)] = 1

graph = [[0] * (N+2) for _ in range(N+2)]
answer = 0
for x,y in cows.keys():
    bfs(x, y)

print(answer//2)