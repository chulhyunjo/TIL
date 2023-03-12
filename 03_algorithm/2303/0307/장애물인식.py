from collections import deque
dx, dy = [0,0,1,-1], [1,-1,0,0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            nx, ny = x + dx[q], y + dy[q]
            if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny]: continue
            elif graph[nx][ny] == '1':
                visited[nx][ny] = 1
                queue.append((nx,ny))
                cnt += 1
    answer.append(cnt)

n = int(input())

graph = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            visited[i][j] = 1
            bfs(i,j)

print(len(answer))
print(*sorted(answer), sep='\n')