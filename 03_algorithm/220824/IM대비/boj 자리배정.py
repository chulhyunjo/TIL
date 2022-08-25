n, m = map(int,input().split())
target = int(input())
graph = [[0] * m for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
x = y = q = 0
result = 0
cnt = 1
while cnt <= n*m:
    graph[x][y] = cnt
    if cnt == target:
        result = [x,y]
        break
    nx = x + dx[q]
    ny = y + dy[q]

    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        x ,y = nx, ny
    else:
        q = (q + 1) % 4
        x = x + dx[q]
        y = y + dy[q]
    cnt += 1

if result:
    print(result[0] + 1, result[1]+1)
else:
    print(0)