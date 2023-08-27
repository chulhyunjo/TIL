from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, 0)])
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(y-2 if y-2>=0 else 0, y+3 if y + 3 < T+1 else T+1):
            for j in range(len(points[i])):
                if abs(x-points[i][j])<=2 and visited[i][j] > cnt+1:
                    if i == T:
                        return cnt + 1
                    visited[i][j] = cnt + 1
                    queue.append((points[i][j],i,cnt + 1))
    return -1

n, T = map(int,input().split())
points = [[] for _ in range(T+1)]
visited = [[] for _ in range(T+1)]
for _ in range(n):
    a, b = map(int,input().split())
    points[b].append(a)
    visited[b].append(n+1)

if not points[-1]:
    print(-1)
else:
    answer = bfs()
    print(answer)