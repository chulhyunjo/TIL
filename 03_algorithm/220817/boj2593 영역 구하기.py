from collections import deque

m,n,k = map(int,input().split())
arr = [[0] *n for _ in range(m)]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = 1
    while queue:
        x,y = queue.popleft()

        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if (0<=nx<m) and (0<=ny<n) and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                result += 1
                queue.append((nx,ny))
    return result


for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2):
        for j in range(x1,x2):
            arr[i][j] = 1

cnt = []

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 1
            cnt.append(bfs(i,j))
print(len(cnt))
print(*sorted(cnt))