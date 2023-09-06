from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(home[0], home[1])])
    while queue:
        x, y = queue.popleft()
        if abs(x-last_x) + abs(y-last_y) <= 1000:
            return 'happy'
        for i in range(N):
            if visited[i]: continue
            nx, ny = position[i]
            if abs(x - nx) + abs(y - ny) <= 1000:
                queue.append((nx,ny))
                visited[i] = True
    return 'sad'

for _ in range(int(input())):
    N = int(input())
    home = list(map(int,input().split()))
    position = []
    for _ in range(N):
        x, y = map(int,input().split())
        position.append((x,y))
    last_x, last_y = map(int,input().split())
    visited = [0] * N
    print(bfs())